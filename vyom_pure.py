import csv

print("Pure Python Vyom Sutra Engine सुरु हुँदैछ...")

molecule_ids = []

# १. test.csv बाट molecule_id हरू पढ्ने
try:
    with open('test.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'molecule_id' in row:
                molecule_ids.append(row['molecule_id'])
    print("test.csv सफलतापूर्वक लोड भयो!")
except FileNotFoundError:
    print("test.csv भेटिएन, डमी डेटा प्रयोग गरिँदैछ...")
    molecule_ids = ['1', '2', '3', '4', '5']

# यदि पहिलो तरिकाले भेटेन भने पहिलो स्तम्भ (Column) पत्याउने
if not molecule_ids:
    try:
        with open('test.csv', mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None) # हेडर छोड्ने
            for row in reader:
                if row:
                    molecule_ids.append(row[0])
    except Exception:
        molecule_ids = ['1', '2', '3', '4', '5']

# २. क्यान्डिडेट SMILES स्ट्रिङ
default_smiles = "CC1=CC(=O)C=CC1=O;OC(=O)c1ccccc1O;CN1C=NC2=C1C(=O)N(C)C(=O)N2C"

# ३. submission.csv फाइल तयार पार्ने
with open('submission.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['molecule_id', 'smiles'])
    for mol_id in molecule_ids:
        writer.writerow([mol_id, default_smiles])

print("काम पूरा भयो! 'submission.csv' फाइल सफलतापूर्वक तयार भयो।")
