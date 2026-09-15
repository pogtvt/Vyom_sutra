<<<<<<< HEAD
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

function resizeCanvas() {
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = canvas.parentElement.clientHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

const WIDTH = canvas.width;
const HEIGHT = canvas.height;
const UI_HEIGHT = canvas.parentElement.querySelector('#ui-panel').clientHeight;
const ARENA_HEIGHT = HEIGHT - UI_HEIGHT;
const RIVER_Y = ARENA_HEIGHT / 2;
const CENTER_X = WIDTH / 2;
const LEFT_BRIDGE_X = WIDTH * 0.28;
const RIGHT_BRIDGE_X = WIDTH * 0.72;

const CARD_POOL = [
    { id: "c1", name: "Quantum Titan", cost: 6, type: "tank", shape: "hexagon", hp: 16000, dmg: 1100, speed: 45, range: 35, radius: 18, count: 5 },
    { id: "c2", name: "Flux Skeletons", cost: 2, type: "swarm", shape: "triangle", hp: 700, dmg: 280, speed: 125, range: 22, radius: 7, count: 20 },
    { id: "c3", name: "Plasma Mage", cost: 4, type: "wizard", shape: "circle", hp: 2900, dmg: 820, speed: 75, range: 165, radius: 12, count: 5 },
    { id: "c4", name: "Tachyonic Knight", cost: 3, type: "melee", shape: "circle", hp: 5800, dmg: 700, speed: 85, range: 28, radius: 14, count: 5 },
    { id: "c5", name: "Codex Spell", cost: 5, type: "spell", dmg: 4200, radius: 130 },
    { id: "c6", name: "Void PEKKA", cost: 7, type: "tank", shape: "hexagon", hp: 18500, dmg: 1650, speed: 40, range: 35, radius: 19, count: 5 }
];

let playerElixir = 5.0, enemyElixir = 5.0;
let matchTimer = 180.0;
let playerHand = [], playerQueue = [], enemyHand = [], enemyQueue = [];
let selectedIndex = null;
let singularityCharge = 0.0;
let towers = [], troops = [], projectiles = [], effects = [];
let aiTimer = 0.0, phaseTheta = 0.0;
let gameState = "BATTLE";

function initGame() {
    playerElixir = 5.0; enemyElixir = 5.0; matchTimer = 180.0;
    singularityCharge = 0.0; selectedIndex = null;
    gameState = "BATTLE";
    document.getElementById('game-over-screen').style.display = 'none';

    let shuffled = [...CARD_POOL].sort(() => Math.random() - 0.5);
    playerHand = shuffled.slice(0, 4);
    playerQueue = shuffled.slice(4, 6);
    enemyHand = [...CARD_POOL].sort(() => Math.random() - 0.5).slice(0, 4);
    enemyQueue = [];

    towers = [
        { x: LEFT_BRIDGE_X, y: ARENA_HEIGHT - 90, team: "player", hp: 16000, maxHp: 16000, radius: 22, isKing: false, active: true },
        { x: RIGHT_BRIDGE_X, y: ARENA_HEIGHT - 90, team: "player", hp: 16000, maxHp: 16000, radius: 22, isKing: false, active: true },
        { x: CENTER_X, y: ARENA_HEIGHT - 40, team: "player", hp: 26000, maxHp: 26000, radius: 28, isKing: true, active: false },
        { x: LEFT_BRIDGE_X, y: 90, team: "enemy", hp: 16000, maxHp: 16000, radius: 22, isKing: false, active: true },
        { x: RIGHT_BRIDGE_X, y: 90, team: "enemy", hp: 16000, maxHp: 16000, radius: 22, isKing: false, active: true },
        { x: CENTER_X, y: 40, team: "enemy", hp: 26000, maxHp: 26000, radius: 28, isKing: true, active: false }
    ];
    troops = []; projectiles = []; effects = [];
    updateUI();
}

class Troop {
    constructor(x, y, team, data) {
        this.x = x; this.y = y; this.team = team; this.data = data;
        this.hp = data.hp; this.maxHp = data.hp;
        this.speed = data.speed; this.dmg = data.dmg;
        this.range = data.range || 25; this.radius = data.radius;
        this.type = data.type; this.shape = data.shape;
        this.cooldown = 0;
        this.lane = x < CENTER_X ? "left" : "right";
    }
    update(dt, enemies) {
        if (this.cooldown > 0) this.cooldown -= dt;
        let target = null, minDist = 999999;

        for (let e of enemies) {
            if (this.lane === "left" && e.x >= CENTER_X) continue;
            if (this.lane === "right" && e.x < CENTER_X) continue;
            let d = Math.hypot(e.x - this.x, e.y - this.y);
            if (d < minDist && d < 40000) { minDist = d; target = e; }
        }

        if (!target) {
            let enemyTowers = towers.filter(t => t.team !== this.team);
            for (let tw of enemyTowers) {
                let d = Math.hypot(tw.x - this.x, tw.y - this.y);
                if (d < minDist) { minDist = d; target = tw; }
            }
        }

        if (target) {
            let dist = Math.hypot(target.x - this.x, target.y - this.y);
            if (dist <= this.range) {
                if (this.cooldown <= 0) {
                    target.hp -= this.dmg;
                    this.cooldown = 1.0;
                }
                return;
            }
        }

        let bridgeX = this.lane === "left" ? LEFT_BRIDGE_X : RIGHT_BRIDGE_X;
        let onOwnSide = (this.team === "player" && this.y > RIVER_Y) || (this.team === "enemy" && this.y < RIVER_Y);
        let destX = onOwnSide ? bridgeX : (target ? target.x : bridgeX);
        let destY = onOwnSide ? RIVER_Y : (target ? target.y : (this.team === "player" ? 40 : ARENA_HEIGHT - 40));

        let dx = destX - this.x, dy = destY - this.y;
        let dist = Math.hypot(dx, dy);
        if (dist > 1) {
            this.x += (dx / dist) * this.speed * dt;
            this.y += (dy / dist) * this.speed * dt;
        }
    }
    draw() {
        ctx.fillStyle = this.team === "player" ? "#00d2ff" : "#ff2850";
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "#fff";
        ctx.stroke();

        let w = this.radius * 2;
        ctx.fillStyle = "#0f141e";
        ctx.fillRect(this.x - w/2, this.y - this.radius - 6, w, 3);
        ctx.fillStyle = this.team === "player" ? "#00ffc8" : "#ff2850";
        ctx.fillRect(this.x - w/2, this.y - this.radius - 6, w * (this.hp / this.maxHp), 3);
    }
}

function triggerSingularity() {
    if (singularityCharge < 100) return;
    singularityCharge = 0;
    troops = troops.filter(t => t.team !== "enemy");
}

canvas.addEventListener('click', (e) => {
    if (gameState !== "BATTLE" || selectedIndex === null) return;
    let rect = canvas.getBoundingClientRect();
    let x = e.clientX - rect.left;
    let y = e.clientY - rect.top;

    let card = playerHand[selectedIndex];
    let isSpell = card.type === "spell";
    let validZone = isSpell || y > RIVER_Y + 10;

    if (validZone && playerElixir >= card.cost) {
        playerElixir -= card.cost;
        if (isSpell) {
            towers.forEach(tw => { if (tw.team === "enemy" && Math.hypot(tw.x - x, tw.y - y) <= card.radius) tw.hp -= card.dmg / 2; });
            troops.forEach(tr => { if (tr.team === "enemy" && Math.hypot(tr.x - x, tr.y - y) <= card.radius) tr.hp -= card.dmg; });
        } else {
            for (let k = 0; k < card.count; k++) {
                let ox = (k % 5 - 2) * 14, oy = (Math.floor(k / 5) - 1) * 14;
                troops.push(new Troop(x + ox, y + oy, "player", card));
            }
        }
        playerHand[selectedIndex] = playerQueue.length ? playerQueue.shift() : CARD_POOL[Math.floor(Math.random()*CARD_POOL.length)];
        selectedIndex = null;
        updateUI();
    }
});

function updateUI() {
    document.getElementById('elixirFill').style.width = `${(playerElixir / 10) * 100}%`;
    document.getElementById('elixirText').innerText = `ENERGY: ${Math.floor(playerElixir)}/10`;
    
    let btn = document.getElementById('k118-btn');
    if (singularityCharge >= 100) btn.classList.add('ready');
    else btn.classList.remove('ready');

    let row = document.getElementById('cardsRow');
    row.innerHTML = '';
    playerHand.forEach((card, idx) => {
        let div = document.createElement('div');
        div.className = `card ${selectedIndex === idx ? 'selected' : ''}`;
        div.innerHTML = `
            <div class="card-title">${card.name.split(' ')[0]}</div>
            <div class="card-count">${card.type === 'spell' ? 'SPELL' : 'x' + card.count}</div>
            <div class="card-cost">${card.cost}</div>
        `;
        div.onclick = () => { selectedIndex = selectedIndex === idx ? null : idx; updateUI(); };
        row.appendChild(div);
    });
}

let lastTime = performance.now();
function gameLoop(now) {
    let dt = (now - lastTime) / 1000;
    lastTime = now;
    dt = Math.min(dt, 0.033);

    if (gameState === "BATTLE") {
        matchTimer -= dt;
        phaseTheta += dt * 1.5;
        singularityCharge = Math.min(100, singularityCharge + dt * 8);
        playerElixir = Math.min(10, playerElixir + 0.5 * dt);
        enemyElixir = Math.min(10, enemyElixir + 0.5 * dt);

        if (matchTimer <= 0) {
            gameState = "GAME_OVER";
            document.getElementById('resultText').innerText = "DRAW!";
            document.getElementById('game-over-screen').style.display = 'flex';
        }

        aiTimer += dt;
        if (aiTimer > 1.2 && enemyElixir >= 4) {
            let card = CARD_POOL[Math.floor(Math.random() * CARD_POOL.length)];
            enemyElixir -= card.cost;
            let tx = Math.random() < 0.5 ? LEFT_BRIDGE_X : RIGHT_BRIDGE_X;
            if (card.type !== 'spell') {
                for (let k = 0; k < card.count; k++) {
                    troops.push(new Troop(tx + (k%5-2)*14, 80 + Math.floor(k/5)*14, "enemy", card));
                }
            }
            aiTimer = 0;
        }

        let pTroops = troops.filter(t => t.team === "player");
        let eTroops = troops.filter(t => t.team === "enemy");
        troops.forEach(tr => tr.update(dt, tr.team === "player" ? eTroops : pTroops));
        troops = troops.filter(tr => tr.hp > 0);

        towers.forEach(tw => {
            if (tw.hp <= 0 && tw.isKing) {
                gameState = "GAME_OVER";
                document.getElementById('resultText').innerText = tw.team === 'player' ? "DEFEAT!" : "VICTORY!";
                document.getElementById('game-over-screen').style.display = 'flex';
            }
        });
        towers = towers.filter(tw => tw.hp > 0);

        ctx.fillStyle = "#04080e";
        ctx.fillRect(0, 0, WIDTH, ARENA_HEIGHT);

        ctx.fillStyle = "#081e34";
        ctx.fillRect(0, RIVER_Y - 16, WIDTH, 32);
        ctx.fillStyle = "#283c5a";
        ctx.fillRect(LEFT_BRIDGE_X - 24, RIVER_Y - 20, 48, 40);
        ctx.fillRect(RIGHT_BRIDGE_X - 24, RIVER_Y - 20, 48, 40);

        if (selectedIndex !== null) {
            ctx.fillStyle = "rgba(0, 255, 180, 0.15)";
            ctx.fillRect(0, RIVER_Y, WIDTH, ARENA_HEIGHT - RIVER_Y);
        }

        towers.forEach(tw => {
            ctx.fillStyle = tw.team === "player" ? "#00d2ff" : "#ff2850";
            ctx.beginPath(); ctx.arc(tw.x, tw.y, tw.radius, 0, Math.PI*2); ctx.fill();
            ctx.strokeStyle = "#fff"; ctx.stroke();
        });

        troops.forEach(tr => tr.draw());
        updateUI();
    }

    requestAnimationFrame(gameLoop);
}

initGame();
requestAnimationFrame(gameLoop);
=======
let audioCtx = null;
let rawBuffer = null;
let synthBuffer = null;
let currentSource = null;

const statusText = document.getElementById('statusText');
const canvas = document.getElementById('visualizer');
const canvasCtx = canvas.getContext('2d');

const paramK = document.getElementById('paramK');
const paramLevel = document.getElementById('paramLevel');
const paramTheta = document.getElementById('paramTheta');
const paramGhost = document.getElementById('paramGhost');

paramK.oninput = () => document.getElementById('kVal').innerText = paramK.value;
paramLevel.oninput = () => document.getElementById('levelVal').innerText = paramLevel.value + '%';
paramTheta.oninput = () => document.getElementById('thetaVal').innerText = paramTheta.value;
paramGhost.oninput = () => document.getElementById('ghostVal').innerText = paramGhost.value;

function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

// Record Audio
document.getElementById('btnRecord').onclick = async () => {
  initAudio();
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    const chunks = [];

    mediaRecorder.ondataavailable = e => chunks.push(e.data);
    mediaRecorder.onstop = async () => {
      const blob = new Blob(chunks, { type: 'audio/wav' });
      const buf = await blob.arrayBuffer();
      rawBuffer = await audioCtx.decodeAudioData(buf);
      readyToSynth("रेकर्डिङ पूरा भयो!");
    };

    mediaRecorder.start();
    statusText.innerText = "अवस्था: बोल्नुहोस् (१.५ सेकेन्ड)...";
    setTimeout(() => mediaRecorder.stop(), 1500);
  } catch (err) {
    alert("माइक्रोफोन चल्न सकेन। 'टेस्ट टोन' थिच्नुहोस्।");
  }
};

// Upload Audio
document.getElementById('fileInput').onchange = async (e) => {
  initAudio();
  const file = e.target.files[0];
  if (!file) return;

  statusText.innerText = "अवस्था: फाइल लोड हुँदैछ...";
  const arrayBuf = await file.arrayBuffer();
  rawBuffer = await audioCtx.decodeAudioData(arrayBuf);
  readyToSynth(`फाइल '${file.name}' तयार भयो!`);
};

// Demo Tone
document.getElementById('btnDemo').onclick = () => {
  initAudio();
  const sr = audioCtx.sampleRate;
  const len = sr * 1.5;
  rawBuffer = audioCtx.createBuffer(1, len, sr);
  const data = rawBuffer.getChannelData(0);

  for (let i = 0; i < len; i++) {
    let t = i / sr;
    data[i] = 0.5 * Math.sin(2 * Math.PI * 220 * t) + 0.25 * Math.sin(2 * Math.PI * 440 * t);
  }
  readyToSynth("टेस्ट टोन तयार भयो!");
};

function readyToSynth(msg) {
  document.getElementById('btnSynthesize').disabled = false;
  statusText.innerText = `अवस्था: ${msg} अब 'सूत्र सिन्थेसाइज' थिच्नुहोस्।`;
  drawWaveform(rawBuffer.getChannelData(0), "#00f2fe");
}

// Fast Mobile Math Engine (Zero-Lag)
document.getElementById('btnSynthesize').onclick = () => {
  if (!rawBuffer) return;
  initAudio();

  const k = parseInt(paramK.value);
  const thetaBase = parseFloat(paramTheta.value);
  const ghost = parseFloat(paramGhost.value);
  const masterGain = parseFloat(paramLevel.value) / 100;

  const sr = rawBuffer.sampleRate;
  const channels = rawBuffer.numberOfChannels;
  const len = rawBuffer.length;

  synthBuffer = audioCtx.createBuffer(channels, len, sr);

  const dyadicW = new Float32Array(k + 1);
  const couplingL = new Float32Array(k + 1);
  let weightSum = 0;

  for (let j = 0; j <= k; j++) {
    dyadicW[j] = Math.pow(2, j);
    couplingL[j] = Math.pow(2, -j / 2);
    weightSum += dyadicW[j] * couplingL[j];
  }

  for (let ch = 0; ch < channels; ch++) {
    const input = rawBuffer.getChannelData(ch);
    const output = synthBuffer.getChannelData(ch);
    let maxPeak = 0.0001;

    for (let i = 0; i < len; i++) {
      let t = i / sr;
      let theta = thetaBase + Math.sin(6.28318 * t);
      let realSum = 0, imagSum = 0;

      for (let j = 0; j <= k; j++) {
        let shiftPos = (i + j * 4) % len;
        let L_j = input[shiftPos];
        let phase = theta * (j + 1);

        realSum += dyadicW[j] * couplingL[j] * L_j * Math.cos(phase);
        imagSum += dyadicW[j] * couplingL[j] * L_j * Math.sin(phase);
      }

      let sig = (realSum + imagSum) / (weightSum || 1);
      let gTerm = -Math.cos(theta) * sig * ghost;
      let val = (sig + gTerm) * masterGain;

      output[i] = val;
      let absV = Math.abs(val);
      if (absV > maxPeak) maxPeak = absV;
    }

    const fadeLen = Math.floor(sr * 0.01);
    let normFactor = maxPeak > 0.85 ? 0.85 / maxPeak : 1.0;

    for (let i = 0; i < len; i++) {
      let v = output[i] * normFactor;
      if (i < fadeLen) v *= (i / fadeLen);
      else if (i > len - fadeLen) v *= ((len - i) / fadeLen);
      output[i] = Math.tanh(v);
    }
  }

  drawWaveform(synthBuffer.getChannelData(0), "#ff007f");
  document.getElementById('btnPlay').disabled = false;

  const dlBtn = document.getElementById('btnDownload');
  const wavBlob = bufferToWave(synthBuffer, synthBuffer.length);
  dlBtn.href = URL.createObjectURL(wavBlob);
  dlBtn.classList.remove('hidden');

  statusText.innerText = "सफलता: सिन्थेसाइज भयो! तलको हरियो बटन थिचेर डाउनलोड गर्नुहोस्।";
};

// Play Audio
document.getElementById('btnPlay').onclick = () => {
  if (!synthBuffer) return;
  initAudio();

  if (currentSource) {
    try { currentSource.stop(); } catch(e){}
  }

  currentSource = audioCtx.createBufferSource();
  currentSource.buffer = synthBuffer;
  currentSource.connect(audioCtx.destination);
  currentSource.start(0);

  statusText.innerText = "अवस्था: आवाज बजिरहेको छ...";
  currentSource.onended = () => statusText.innerText = "अवस्था: प्ले समाप्त भयो।";
};

// WAV Encoder
function bufferToWave(abuffer, len) {
  let numOfChan = abuffer.numberOfChannels,
      length = len * numOfChan * 2 + 44,
      out = new DataView(new ArrayBuffer(length)),
      channels = [], i, sample, offset = 0, pos = 0;

  function setUint16(d) { out.setUint16(pos, d, true); pos += 2; }
  function setUint32(d) { out.setUint32(pos, d, true); pos += 4; }

  setUint32(0x46464952); // "RIFF"
  setUint32(length - 8);
  setUint32(0x45564157); // "WAVE"
  setUint32(0x20746d66); // "fmt "
  setUint32(16);
  setUint16(1);          // PCM
  setUint16(numOfChan);
  setUint32(abuffer.sampleRate);
  setUint32(abuffer.sampleRate * 2 * numOfChan);
  setUint16(numOfChan * 2);
  setUint16(16);
  setUint32(0x61746164); // "data"
  setUint32(length - pos - 4);

  for (i = 0; i < abuffer.numberOfChannels; i++) channels.push(abuffer.getChannelData(i));

  while (offset < len) {
    for (i = 0; i < numOfChan; i++) {
      sample = Math.max(-1, Math.min(1, channels[i][offset]));
      sample = (0.5 + sample < 0 ? sample * 32768 : sample * 32767) | 0;
      out.setInt16(pos, sample, true); pos += 2;
    }
    offset++;
  }
  return new Blob([out], { type: "audio/wav" });
}

// Draw Waveform
function drawWaveform(data, color) {
  canvasCtx.fillStyle = "#020307";
  canvasCtx.fillRect(0, 0, canvas.width, canvas.height);
  canvasCtx.lineWidth = 2;
  canvasCtx.strokeStyle = color;
  canvasCtx.beginPath();

  const sliceWidth = canvas.width / data.length;
  let x = 0;

  for (let i = 0; i < data.length; i += 30) {
    const v = data[i];
    const y = (v + 1) * (canvas.height / 2);
    if (i === 0) canvasCtx.moveTo(x, y);
    else canvasCtx.lineTo(x, y);
    x += sliceWidth * 30;
  }
  canvasCtx.lineTo(canvas.width, canvas.height / 2);
  canvasCtx.stroke();
}
>>>>>>> c0e1f1c (feat: split web synthesizer into index.html, style.css, and script.js)
