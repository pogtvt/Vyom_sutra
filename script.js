const canvas = document.getElementById('waveCanvas');
const ctx = canvas.getContext('2d');

let freqSlider = document.getElementById('freqSlider');
let freqVal = document.getElementById('freqVal');
let ampSlider = document.getElementById('ampSlider');
let ampVal = document.getElementById('ampVal');

let time = 0;
const uniformColor = "#38bdf8";

const states = [
    { key: 'dark', maxFreq: 2.5, name: "Dark Energy (Ultra-Long wavelength)", short: "Dark Energy", def: "Ultra-Long Wavelength -> Undetectable Wave Field", scale: "Ultra-Long", detect: "Undetectable", topo: "0 ⇌ Loop" },
    { key: 'gravity', maxFreq: 6.0, name: "Gravity (Very Weak Force Field)", short: "Gravity", def: "Very weak Force Field (Subtle Curvature)", scale: "Medium Hz", detect: "Measurable", topo: "0 ⇌ Loop" },
    { key: 'particle', maxFreq: 15.0, name: "Particle State (Standard Propagation)", short: "Particle State", def: "Standard Wave Propagation & Observation", scale: "Standard Hz", detect: "Observable", topo: "0 ⇌ Loop" },
    { key: 'bh', maxFreq: 25.0, name: "Black Hole (Packed Sine Waves)", short: "Black Hole", def: "Packed Sine Waves (Extreme Compression)", scale: "Packed Sine", detect: "Extreme Comp.", topo: "0 ⇌ Loop" }
];

function updateUI(freq) {
    let current = states.find(s => freq <= s.maxFreq) || states[states.length - 1];

    document.getElementById('stateName').innerText = current.name;
    document.getElementById('stateDef').innerText = current.def;
    document.getElementById('mState').innerText = current.short;
    document.getElementById('mScale').innerText = current.scale;
    document.getElementById('mDetect').innerText = current.detect;
    document.getElementById('mTopo').innerText = current.topo;

    document.querySelectorAll('.btn-grid button').forEach(b => b.classList.remove('active'));
    let activeBtn = document.getElementById('btn-' + current.key);
    if(activeBtn) activeBtn.classList.add('active');
}

function setMode(key, freqValTarget) {
    freqSlider.value = freqValTarget;
    freqVal.innerText = freqValTarget;
    updateUI(freqValTarget);
}

freqSlider.addEventListener('input', (e) => {
    let val = parseFloat(e.target.value);
    freqVal.innerText = val;
    updateUI(val);
});

ampSlider.addEventListener('input', (e) => {
    ampVal.innerText = e.target.value;
});

function resizeCanvas() {
    canvas.width = canvas.parentElement.clientWidth - 48;
    canvas.height = 260;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function drawWave() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    ctx.strokeStyle = '#111827';
    ctx.lineWidth = 1;
    for(let i = 0; i < canvas.width; i += 45) {
        ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
    }
    for(let j = 0; j < canvas.height; j += 45) {
        ctx.beginPath(); ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); ctx.stroke();
    }

    let freq = parseFloat(freqSlider.value);
    let amp = parseFloat(ampSlider.value);

    ctx.beginPath();
    ctx.lineWidth = 3.5;
    ctx.strokeStyle = uniformColor;
    
    ctx.shadowBlur = 18;
    ctx.shadowColor = uniformColor;

    let centerY = canvas.height / 2;
    for (let x = 0; x < canvas.width; x++) {
        let y = centerY + Math.sin((x * 0.018 * freq) + time) * amp * (freq / 6 > 1 ? 1 : freq/6);
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.shadowBlur = 0;

    time += 0.04 * (freq * 0.35);
    requestAnimationFrame(drawWave);
}

drawWave();
