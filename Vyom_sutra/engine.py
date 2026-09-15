import os
import json
import re
import random
import threading
import time
from pathlib import Path
from .core import VyomSutraCore, THEMES

BASE_DIR = Path("/sdcard/SutraAI") if os.path.exists("/sdcard") and os.access("/sdcard", os.W_OK) else Path.home() / ".sutra_ai"
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)
MODEL_FILE = str(MODEL_DIR / "sutra_llm_weights.json")

class VyomSutraLLM:
    def __init__(self):
        self.transitions = {}
        self.vocab = set()
        self.lock = threading.Lock()
        self.temperature = 0.70
        self.top_k = 40
        self.top_p = 0.88
        self.repetition_penalty = 2.50

    def clean_text(self, text):
        cleanr = re.compile('<.*?>')
        text = re.sub(cleanr, ' ', text)
        return re.sub(r'[^a-zA-Z\s]', ' ', text).lower()

    def get_context_phase(self, word_list):
        if not word_list:
            return 0.0
        recent = word_list[-6:]
        weighted_sum = sum(VyomSutraCore.calculate_token_phase(w) for w in recent)
        return (weighted_sum / len(recent)) % (2.0 * VyomSutraCore.PI)

    def load_weights(self, filepath=MODEL_FILE):
        if os.path.exists(filepath):
            try:
                with self.lock:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        self.transitions = data.get("transitions", data)
                        self.vocab = set(self.transitions.keys())
                return True
            except Exception:
                pass
        return False

    def save_checkpoint(self, filepath=MODEL_FILE):
        with self.lock:
            payload = {
                "metadata": {"vocab_size": len(self.vocab), "saved_at": time.strftime("%Y-%m-%d %H:%M:%S")},
                "transitions": self.transitions
            }
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(payload, f, indent=2)
            except Exception:
                pass

    def learn_text(self, raw_text):
        text = self.clean_text(raw_text)
        tokens = text.split()
        if len(tokens) < 2:
            return 0
        added = 0
        with self.lock:
            for i in range(len(tokens) - 1):
                w1, w2 = tokens[i], tokens[i+1]
                self.vocab.add(w1)
                self.vocab.add(w2)
                if w1 not in self.transitions:
                    self.transitions[w1] = {}
                self.transitions[w1][w2] = self.transitions[w1].get(w2, 0) + 1
                added += 1
        self.save_checkpoint()
        return added

    def sample_next_token(self, context_words, generated_words):
        if not context_words:
            return None
        current_word = context_words[-1]

        with self.lock:
            if current_word not in self.transitions:
                return None
            candidates = dict(self.transitions[current_word])

        ctx_phase = self.get_context_phase(context_words)
        modulated_probs = {}

        for token, count in candidates.items():
            t_phase = VyomSutraCore.calculate_token_phase(token)
            res_p, _ = VyomSutraCore.compute_resonance(ctx_phase, t_phase)

            if token in generated_words:
                count /= self.repetition_penalty

            score = (count * res_p) ** (1.0 / max(self.temperature, 0.05))
            if score > 0:
                modulated_probs[token] = score

        if not modulated_probs:
            return random.choice(list(candidates.keys()))

        sorted_cands = sorted(modulated_probs.items(), key=lambda x: x[1], reverse=True)[:self.top_k]
        tokens = [x[0] for x in sorted_cands]
        weights = [x[1] for x in sorted_cands]
        return random.choices(tokens, weights=weights, k=1)[0]

    def generate_text_stream(self, prompt, length=40):
        words = self.clean_text(prompt).split()
        if not words:
            yield "Empty prompt."
            return

        context = list(words)
        generated = []

        for _ in range(length):
            next_tok = self.sample_next_token(context, generated)
            if not next_tok:
                break
            yield next_tok + " "
            context.append(next_tok)
            generated.append(next_tok)

        if len(generated) > 2:
            self.learn_text(f"{prompt} {' '.join(generated)}")
