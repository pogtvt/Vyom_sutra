const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const FOV = 280;
const HALF_W = canvas.width / 2;
const HALF_H = canvas.height / 2;

let score = 0, combo = 0, slicedCount = 0, totalSpawned = 0, frameCount = 0;
let cameraShake = 0;
let audioEnabled = true;

let audioCtx = null;
function initAudioAndStart() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    document.getElementById('start-overlay').style.display = 'none';
}

function playCyberSlashSound(isRed) {
    if (!audioCtx || !audioEnabled) return;
    let osc = audioCtx.createOscillator();
    let gain = audioCtx.createGain();
    osc.type = 'sawtooth';
    let freq = isRed ? 850 : 1100;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(80, audioCtx.currentTime + 0.12);
    gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.12);
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.start(); osc.stop(audioCtx.currentTime + 0.12);
}

function playBassBeat(freq) {
    if (!audioCtx || !audioEnabled) return;
    let osc = audioCtx.createOscillator();
    let gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.2);
    osc.connect(gain); gain.connect(audioCtx.destination);
    osc.start(); osc.stop(audioCtx.currentTime + 0.2);
}

function toggleAudio() { audioEnabled = !audioEnabled; }

function vyomScore(v, t, s = 1.0) {
    let theta = ((v % Math.PI) + Math.PI) % Math.PI;
    let d = Math.abs(t - theta);
    let S = Math.cos(d * s) * 100;
    return { theta, d, score: Math.max(0, S), verdict: S > 95 ? "Excellent" : "Clean" };
}

function project3D(x, y, z) {
    const scale = FOV / (FOV + z);
    return { x: HALF_W + x * scale, y: HALF_H + y * scale, scale: scale };
}

const flyAgent = {
    x: 0, y: 110, z: 40,
    leftAngle: 0, rightAngle: 0,
    leftHistory: [], rightHistory: []
};

let blocks = [];
let splitPieces = [];
let particles = [];
let shockwaves = [];
const directions = ['↑', '↓', '←', '→'];

function spawn3DBlock() {
    const lanesX = [-180, -60, 60, 180];
    const laneX = lanesX[Math.floor(Math.random() * lanesX.length)];
    const color = Math.random() > 0.5 ? '#ff0055' : '#00ccff';
    const dir = directions[Math.floor(Math.random() * directions.length)];

    blocks.push({
        x: laneX, y: -20, z: 850,
        speed: 9.5 + Math.random() * 3,
        size: 75, color: color, dir: dir, sliced: false
    });
    totalSpawned++;
}

function resetGame() {
    score = 0; combo = 0; slicedCount = 0; totalSpawned = 0;
    blocks = []; splitPieces = []; particles = []; shockwaves = [];
}

function triggerSliceEffects(b, saberAngle) {
    cameraShake = 8;
    playCyberSlashSound(b.color === '#ff0055');

    for (let side = -1; side <= 1; side += 2) {
        splitPieces.push({
            x: b.x + side * 20, y: b.y, z: b.z,
            vx: side * (7 + Math.random() * 4), vy: -5 - Math.random() * 3, vz: -b.speed * 0.4,
            size: b.size * 0.5, color: b.color, angle: saberAngle, rotSpeed: side * 0.2, life: 1.0
        });
    }
    for (let i = 0; i < 18; i++) {
        particles.push({
            x: b.x, y: b.y, z: b.z,
            vx: (Math.random() - 0.5) * 18, vy: (Math.random() - 0.5) * 18, vz: (Math.random() - 0.5) * 14,
            color: b.color, life: 1.0
        });
    }
    shockwaves.push({ x: b.x, y: b.y, z: b.z, radius: 10, color: b.color, alpha: 1.0 });
}

function render() {
    frameCount++;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.save();
    if (cameraShake > 0) {
        let rx = (Math.random() - 0.5) * cameraShake;
        let ry = (Math.random() - 0.5) * cameraShake;
        ctx.translate(rx, ry);
        cameraShake *= 0.85;
    }

    if (frameCount % 16 === 0) {
        let vyomWaveNote = 60 + Math.sin(frameCount * 0.05) * 20;
        playBassBeat(vyomWaveNote);
    }

    ctx.lineWidth = 2;
    for (let i = -420; i <= 420; i += 20) {
        let waveY = HALF_H + 200 + Math.sin(i * 0.01 + frameCount * 0.08) * 18;
        ctx.strokeStyle = `rgba(0, 255, 204, 0.15)`;
        ctx.beginPath(); ctx.moveTo(HALF_W + i, HALF_H + 220); ctx.lineTo(HALF_W + i, waveY); ctx.stroke();
    }

    for (let z = 900; z >= 0; z -= 90) {
        let p1 = project3D(-280, 180, z);
        let p2 = project3D(280, 180, z);
        let alpha = (900 - z) / 900;
        ctx.strokeStyle = `rgba(0, 255, 204, ${alpha * 0.3})`;
        ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
    }
    [-280, -90, 90, 280].forEach(lx => {
        let pNear = project3D(lx, 180, 0);
        let pFar = project3D(lx, 180, 900);
        ctx.strokeStyle = 'rgba(0, 255, 204, 0.45)';
        ctx.beginPath(); ctx.moveTo(pNear.x, pNear.y); ctx.lineTo(pFar.x, pFar.y); ctx.stroke();
    });

    if (frameCount % 26 === 0) spawn3DBlock();

    let bestVyomResult = { theta: 0, d: 0, score: 100, verdict: 'Excellent' };
    let flyP = project3D(flyAgent.x, flyAgent.y, flyAgent.z);

    let targetBlock = null;
    let minDist = 9999;
    for (let b of blocks) {
        if (!b.sliced && b.z > 20 && b.z < 350) {
            if (b.z < minDist) { minDist = b.z; targetBlock = b; }
        }
    }

    if (targetBlock) {
        let blockP = project3D(targetBlock.x, targetBlock.y, targetBlock.z);
        let dx = blockP.x - flyP.x;
        let dy = blockP.y - flyP.y;
        let exactAngle = Math.atan2(-dy, dx);
        let targetPhase = ((exactAngle % Math.PI) + Math.PI) % Math.PI;

        bestVyomResult = vyomScore(exactAngle, targetPhase, 1.0);

        if (targetBlock.color === '#ff0055') flyAgent.leftAngle = exactAngle;
        else flyAgent.rightAngle = exactAngle;

        if (targetBlock.z < 160) {
            targetBlock.sliced = true;
            score += 250 + combo * 25; combo++; slicedCount++;
            triggerSliceEffects(targetBlock, exactAngle);
        }
    } else {
        flyAgent.leftAngle = 2.2 + Math.sin(frameCount * 0.08) * 0.1;
        flyAgent.rightAngle = 0.9 - Math.sin(frameCount * 0.08) * 0.1;
    }

    let accuracy = totalSpawned > 0 ? ((slicedCount / totalSpawned) * 100).toFixed(1) : "100.0";
    document.getElementById('accuracyVal').innerText = accuracy + '%';
    document.getElementById('thetaVal').innerText = bestVyomResult.theta.toFixed(3) + ' rad';
    document.getElementById('diffVal').innerText = bestVyomResult.d.toFixed(3);
    document.getElementById('scoreSVal').innerText = bestVyomResult.score.toFixed(2) + '%';
    document.getElementById('scoreVal').innerText = score;
    document.getElementById('comboVal').innerText = combo + 'x';
    document.getElementById('sliceVal').innerText = slicedCount;

    blocks.sort((a, b) => b.z - a.z);
    for (let i = blocks.length - 1; i >= 0; i--) {
        let b = blocks[i];
        b.z -= b.speed;
        if (!b.sliced && b.z > 0) {
            let p = project3D(b.x, b.y, b.z);
            let sz = b.size * p.scale;
            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.fillStyle = b.color;
            ctx.shadowColor = b.color; ctx.shadowBlur = 25 * p.scale;
            ctx.fillRect(-sz/2, -sz/2, sz, sz);
            ctx.fillStyle = '#ffffff';
            ctx.fillRect(-sz/3, -sz/3, sz/1.5, sz/1.5);
            ctx.fillStyle = '#000000';
            ctx.font = `bold ${Math.max(10, 22 * p.scale)}px sans-serif`;
            ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
            ctx.fillText(b.dir, 0, 0);
            ctx.restore();
        }
        if (b.z <= 0) { if (!b.sliced) combo = 0; blocks.splice(i, 1); }
    }

    for (let i = shockwaves.length - 1; i >= 0; i--) {
        let sw = shockwaves[i];
        sw.radius += 6; sw.alpha -= 0.04;
        if (sw.alpha > 0) {
            let p = project3D(sw.x, sw.y, sw.z);
            ctx.strokeStyle = sw.color; ctx.lineWidth = 3; ctx.globalAlpha = sw.alpha;
            ctx.beginPath(); ctx.arc(p.x, p.y, sw.radius * p.scale, 0, Math.PI * 2); ctx.stroke();
            ctx.globalAlpha = 1.0;
        } else shockwaves.splice(i, 1);
    }

    for (let i = splitPieces.length - 1; i >= 0; i--) {
        let sp = splitPieces[i];
        sp.x += sp.vx; sp.y += sp.vy; sp.z += sp.vz; sp.life -= 0.035; sp.angle += sp.rotSpeed;
        if (sp.life > 0) {
            let p = project3D(sp.x, sp.y, sp.z);
            let sz = sp.size * p.scale;
            ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(sp.angle);
            ctx.fillStyle = sp.color; ctx.globalAlpha = sp.life;
            ctx.fillRect(-sz/2, -sz/2, sz, sz);
            ctx.restore();
        } else splitPieces.splice(i, 1);
    }

    for (let i = particles.length - 1; i >= 0; i--) {
        let pt = particles[i];
        pt.x += pt.vx; pt.y += pt.vy; pt.z += pt.vz; pt.life -= 0.05;
        if (pt.life > 0) {
            let p = project3D(pt.x, pt.y, pt.z);
            ctx.fillStyle = pt.color; ctx.globalAlpha = pt.life;
            ctx.fillRect(p.x, p.y, 5 * p.scale, 5 * p.scale);
        } else particles.splice(i, 1);
    }

    ctx.fillStyle = '#0a0d1a'; ctx.strokeStyle = '#00ffcc'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(flyP.x, flyP.y, 18 * flyP.scale, 0, Math.PI * 2); ctx.fill(); ctx.stroke();

    ctx.fillStyle = '#ff0055'; ctx.shadowColor = '#ff0055'; ctx.shadowBlur = 10;
    ctx.beginPath();
    ctx.arc(flyP.x - 8 * flyP.scale, flyP.y - 6 * flyP.scale, 5 * flyP.scale, 0, Math.PI * 2);
    ctx.arc(flyP.x + 8 * flyP.scale, flyP.y - 6 * flyP.scale, 5 * flyP.scale, 0, Math.PI * 2);
    ctx.fill(); ctx.shadowBlur = 0;

    const drawHyperSaber = (originX, originY, angle, color, history) => {
        let saberLen = 110 * flyP.scale;
        let tipX = originX + Math.cos(angle) * saberLen;
        let tipY = originY - Math.sin(angle) * saberLen;

        history.push({ x: tipX, y: tipY });
        if (history.length > 8) history.shift();

        ctx.beginPath();
        for (let i = 0; i < history.length; i++) ctx.lineTo(history[i].x, history[i].y);
        ctx.strokeStyle = color; ctx.lineWidth = 12 * flyP.scale; ctx.globalAlpha = 0.25;
        ctx.stroke(); ctx.globalAlpha = 1.0;

        ctx.strokeStyle = color; ctx.shadowColor = color; ctx.shadowBlur = 30; ctx.lineWidth = 7 * flyP.scale;
        ctx.beginPath(); ctx.moveTo(originX, originY); ctx.lineTo(tipX, tipY); ctx.stroke();
        ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 3 * flyP.scale;
        ctx.beginPath(); ctx.moveTo(originX, originY); ctx.lineTo(tipX, tipY); ctx.stroke();
        ctx.shadowBlur = 0;
    };

    drawHyperSaber(flyP.x - 14 * flyP.scale, flyP.y, flyAgent.leftAngle, '#ff0055', flyAgent.leftHistory);
    drawHyperSaber(flyP.x + 14 * flyP.scale, flyP.y, flyAgent.rightAngle, '#00ccff', flyAgent.rightHistory);

    ctx.restore();
    requestAnimationFrame(render);
}

render();
