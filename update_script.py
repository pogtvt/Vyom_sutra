with open("drug_discovery.html", "r") as f:
    content = f.read()

admet_code = """
<div style="margin-top: 15px; padding: 12px; background: rgba(0, 255, 200, 0.05); border: 1px solid #00ffcc; border-radius: 8px;">
    <h4 style="color: #00ffcc; margin: 0 0 8px 0;">O(1) ADMET & Toxicity Profile</h4>
    <p style="margin: 4px 0; font-size: 0.85rem;">Absorption Rate: <b id="absVal">84.2%</b> | BBB Status: <b id="bbbVal">PASS</b></p>
    <p style="margin: 4px 0; font-size: 0.85rem;">Off-Target Toxicity Risk: <b id="toxVal" style="color: #ff5555;">12.4%</b></p>
</div>
"""

if "O(1) ADMET & Toxicity Profile" not in content:
    content = content.replace('</div>\n\n<div class="card"', admet_code + '</div>\n\n<div class="card"', 1)

with open("drug_discovery.html", "w") as f:
    f.write(content)

