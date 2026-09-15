import time
import json
import os
import math
import subprocess
import random

DATA_FILE = "discoveries.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

COMPOUND_DATABASE = [
    {"name": "Nazartinib / EGF816", "cid": 78357754, "mw": 463.9, "logp": 2.8},
    {"name": "Gefitinib (1st Gen)", "cid": 123631, "mw": 446.9, "logp": 3.2},
    {"name": "Erlotinib (1st Gen)", "cid": 176870, "mw": 393.4, "logp": 3.3},
    {"name": "Sunitinib (Multi-Kinase)", "cid": 5329102, "mw": 398.5, "logp": 3.1},
    {"name": "Dacomitinib (2nd Gen)", "cid": 11524144, "mw": 469.9, "logp": 3.3},
    {"name": "Osimertinib (3rd Gen)", "cid": 71496458, "mw": 499.6, "logp": 3.9},
    {"name": "Sotorasib (KRAS G12C)", "cid": 138338662, "mw": 560.6, "logp": 2.8},
    {"name": "Alectinib (ALK)", "cid": 49806720, "mw": 483.6, "logp": 4.6},
    {"name": "Vandetanib (VEGFR/EGFR)", "cid": 3081361, "mw": 475.4, "logp": 4.8},
    {"name": "Amoxicillin (Control)", "cid": 33613, "mw": 365.4, "logp": 0.9},
    {"name": "Ibuprofen (Control)", "cid": 3672, "mw": 206.28, "logp": 3.5},
    {"name": "Aspirin (Control)", "cid": 2244, "mw": 180.16, "logp": 1.2},
    {"name": "Metformin (Control)", "cid": 4091, "mw": 129.16, "logp": -1.4}
]

def evaluate_vyom_sutra(compound, theta_target=1.2566):
    mw = compound["mw"]
    logp = compound["logp"]
    
    theta_l = ((mw / 500.0) * 1.1 + (logp / 5.0) * 0.5) % math.pi
    c_mu_nu = math.sin(abs(theta_target - theta_l)) * 50.0
    resonance_p = math.exp(-2.0 * ((theta_target - theta_l) ** 2)) * 100.0
    
    if c_mu_nu < 15.0:
        status = "Clean Target Hit"
    elif c_mu_nu < 20.0:
        status = "Moderate Hit"
    else:
        status = "Filtered Noise"
        
    return {
        "id": f"CID-{compound['cid']}",
        "name": compound['name'],
        "mw": mw,
        "logp": logp,
        "phase_angle": round(theta_l, 4),
        "c_mu_nu": round(c_mu_nu, 2),
        "affinity_score": round(resonance_p, 2),
        "status": status,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def save_and_push(result):
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    
    # लिमिट हटाइयो: सबै डिस्कभरीहरू सधैँ एड हुन्छन् (Unlimited History)
    data.insert(0, result)
        
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"[Vyom Engine] Screened: {result['name']} | Resonance: {result['affinity_score']}% | Status: {result['status']}")
    
    try:
        subprocess.run(["git", "add", DATA_FILE], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", f"Auto-discovery: {result['name']}"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "push"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[GitHub Sync] Pushed successfully!\n")
    except Exception as e:
        print(f"[Git Sync Notice]: Waiting for network or queued ({e})\n")

def background_loop():
    print("🧬 Vyom Sutra Autonomous Engine Started (5s interval, Unlimited History)...")
    while True:
        compound = random.choice(COMPOUND_DATABASE)
        result = evaluate_vyom_sutra(compound)
        save_and_push(result)
        time.sleep(5) # हरेक ५ सेकेन्डमा अल्ट्रा-फास्ट स्क्रीनिङ

if __name__ == "__main__":
    background_loop()
