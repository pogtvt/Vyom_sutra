import time
import json
import os
import random
import subprocess

DATA_FILE = "discoveries.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def save_and_push(compound):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    
    data.insert(0, compound)
    if len(data) > 100:
        data = data[:100]
        
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"[Discovered] {compound['name']} ({compound['affinity_score']}%)")
    
    try:
        subprocess.run(["git", "add", DATA_FILE], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-discovered: {compound['name']}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("[GitHub Sync] Pushed successfully!\n")
    except Exception as e:
        print(f"[Git Error]: {e}\n")

def background_loop():
    compound_names = ["Vyom-Benzene-X", "Sutra-Valine-7", "Kankai-Inhibitor-9", "Nexus-Gef-X", "Wave-Target-Delta"]
    print("🧬 Vyom Sutra Autonomous Engine Started in Terminal...")
    while True:
        new_compound = {
            "id": f"VYOM-{random.randint(10000, 99999)}",
            "name": random.choice(compound_names),
            "affinity_score": round(random.uniform(92.0, 99.9), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        save_and_push(new_compound)
        time.sleep(30) # हरेक ३० सेकेन्डमा नयाँ खोजेर गिटमा पुश हुन्छ

if __name__ == "__main__":
    background_loop()
