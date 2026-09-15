import json
import os
import math
import random
import time

DATA_FILE = "discoveries.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

BENCHMARK_DATABASE = [
    {"name": "Nazartinib / EGF816", "cid": "CID-78357754", "mw": 463.9, "logp": 2.8, "type": "Benchmark"},
    {"name": "Osimertinib (3rd Gen)", "cid": "CID-71496458", "mw": 499.6, "logp": 3.9, "type": "Benchmark"},
    {"name": "Gefitinib (1st Gen)", "cid": "CID-123631", "mw": 446.9, "logp": 3.2, "type": "Benchmark"},
    {"name": "Sunitinib (Multi-Kinase)", "cid": "CID-5329102", "mw": 398.5, "logp": 3.1, "type": "Benchmark"},
    {"name": "Dacomitinib (2nd Gen)", "cid": "CID-11524144", "mw": 469.9, "logp": 3.3, "type": "Benchmark"}
]

def generate_dyadic_inverse_compound(theta_target=1.2566):
    logp = round(random.uniform(2.2, 4.0), 2)
    term = theta_target - (logp / 5.0) * 0.5
    mw = round((term / 1.1) * 500.0, 2)
    
    if mw < 340 or mw > 540:
        mw = round(random.uniform(380.0, 480.0), 2)
        
    k_resolution = random.choice([32, 64, 128, 256, 65536])
    name = f"Vyom-Sutra-k{k_resolution}-{random.randint(100, 999)}"
    
    sa_score = round(9.8 - (abs(mw - 450) / 90.0), 1)
    sa_score = max(7.5, min(9.9, sa_score))
    
    return {
        "name": name,
        "cid": f"VYOM-GEN-{random.randint(10000, 99999)}",
        "mw": mw,
        "logp": logp,
        "sa_score": sa_score,
        "type": "Dyadic Inverse Generated"
    }

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
        "id": compound['cid'],
        "name": compound['name'],
        "type": compound['type'],
        "mw": mw,
        "logp": logp,
        "phase_angle": round(theta_l, 4),
        "c_mu_nu": round(c_mu_nu, 2),
        "affinity_score": round(resonance_p, 2),
        "sa_score": compound.get("sa_score", 9.5),
        "status": status,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    # प्रत्येक क्लाउड रनमा ३ वटा नयाँ कम्पाउन्ड थप्ने
    for _ in range(3):
        if random.random() > 0.5:
            compound = random.choice(BENCHMARK_DATABASE)
        else:
            compound = generate_dyadic_inverse_compound()
            
        result = evaluate_vyom_sutra(compound)
        data.insert(0, result)
        print(f"[Cloud Generated] {result['name']} | Resonance: {result['affinity_score']}%")

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
        
    print("Successfully updated discoveries.json on Cloud!")

if __name__ == "__main__":
    main()
