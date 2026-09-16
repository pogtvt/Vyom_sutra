// Vyom Sutra O(1) ADMET & Toxicity Engine
function computeO1ADMET(mw, logp, phaseRad, tensorVal) {
    const absScore = (1 / (1 + Math.exp(0.5 * (logp - 3)))) * Math.abs(Math.cos(phaseRad));
    const bbbPass = (logp >= 2.0 && logp <= 4.2 && mw < 480) ? "PASS" : "RESTRICTED";
    const toxRisk = Math.abs(Math.sin((Math.PI * mw / 600) + tensorVal)) * 30;
    const qedScore = Math.max(10, ((100 - toxRisk) * (0.7 + absScore * 0.3))).toFixed(1);

    return {
        absorption: (absScore * 100).toFixed(1) + "%",
        bbbStatus: bbbPass,
        toxicityRisk: toxRisk.toFixed(1) + "%",
        overallScore: qedScore
    };
}
