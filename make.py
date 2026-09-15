import os

os.makedirs("Disaster_prediction", exist_ok=True)

# 1. Master Hub (index.html)
with open("index.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vyom Sutra Master Dashboard Hub</title>
    <style>
        body { background: #030712; color: #f3f4f6; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        .container { max-width: 650px; width: 100%; background: rgba(15, 23, 42, 0.95); border: 1px solid #38bdf8; border-radius: 12px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); }
        h1 { color: #38bdf8; text-align: center; font-size: 20px; margin-bottom: 5px; }
        p { text-align: center; color: #94a3b8; font-size: 12px; }
        .section-title { font-size: 14px; border-bottom: 1px solid #1e293b; padding-bottom: 6px; margin-top: 20px; }
        ul { list-style: none; padding: 0; margin: 10px 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; font-weight: bold; padding: 12px 15px; border-radius: 8px; display: block; transition: 0.2s; font-size: 14px; text-align: center; }
        .critical-link { border: 2px solid #ef4444; color: #ef4444; background: rgba(239, 68, 68, 0.15); }
        .critical-link:hover { background: #ef4444; color: #030712; }
        .normal-link { border: 1px solid #38bdf8; color: #38bdf8; background: #1e293b; }
        .normal-link:hover { background: #38bdf8; color: #030712; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Vyom Sutra Dashboard Hub</h1>
        <p>Ultra-Fast Wave-Based Decision, Signal Processing & Simulation Engine</p>
        
        <h3 class="section-title" style="color: #ef4444;">🚨 1. Critical Early-Warning Systems (Highest Priority)</h3>
        <ul>
            <li><a href="Disaster_prediction/Disaster_prediction.html" class="critical-link">🚨 Critical Disaster Prediction System</a></li>
        </ul>

        <h3 class="section-title" style="color: #a855f7;">🌌 2. Core Simulations & Games (High Priority)</h3>
        <ul>
            <li><a href="universe_simulation.html" class="normal-link">🌌 Universe Simulation Engine</a></li>
            <li><a href="fast_decision_npc_game.html" class="normal-link">🕹️ Fast Decision & NPC Game</a></li>
        </ul>

        <h3 class="section-title" style="color: #38bdf8;">🎛️ 3. Synthesizers & Physics Games</h3>
        <ul>
            <li><a href="synth.html" class="normal-link">🎛️ Vyom Wave Synthesizer</a></li>
            <li><a href="badminton.html" class="normal-link">🏸 Badminton Physics Simulation Game</a></li>
        </ul>
    </div>
</body>
</html>""")

# 2. Disaster Prediction
with open("Disaster_prediction/Disaster_prediction.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Disaster Prediction System</title>
    <style>
        body { background: #030712; color: #f3f4f6; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        .box { background: rgba(15, 23, 42, 0.95); border: 2px solid #ef4444; border-radius: 12px; padding: 30px; max-width: 600px; width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.8); text-align: center; }
        h1 { color: #ef4444; font-size: 20px; }
        a { color: #38bdf8; text-decoration: none; display: inline-block; margin-top: 20px; font-weight: bold; background: #1e293b; padding: 10px 15px; border-radius: 6px; border: 1px solid #38bdf8; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚨 Critical Disaster Prediction Early-Warning System</h1>
        <p style="color: #10b981; font-weight: bold;">System Active & Monitoring Wave Signals in Real-Time</p>
        <p style="color: #94a3b8; font-size: 13px;">Processing real-time wave telemetry and critical anomaly detection algorithms.</p>
        <a href="../index.html">← Back to Dashboard Hub</a>
    </div>
</body>
</html>""")

# 3. Universe Simulation
with open("universe_simulation.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Universe Simulation Engine</title>
    <style>
        body { background: #030712; color: #f3f4f6; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        .box { background: rgba(15, 23, 42, 0.95); border: 1px solid #38bdf8; border-radius: 12px; padding: 30px; max-width: 600px; width: 100%; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.8); }
        h1 { color: #38bdf8; font-size: 20px; }
        a { color: #38bdf8; text-decoration: none; display: inline-block; margin-top: 20px; font-weight: bold; background: #1e293b; padding: 10px 15px; border-radius: 6px; border: 1px solid #38bdf8; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🌌 Universe Simulation Engine</h1>
        <p style="color: #10b981;">Scale-Summation & Cosmic Field Wave Simulation Active</p>
        <a href="index.html">← Back to Dashboard Hub</a>
    </div>
</body>
</html>""")

# 4. NPC Game
with open("fast_decision_npc_game.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fast Decision & NPC Game</title>
    <style>
        body { background: #030712; color: #f3f4f6; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        .box { background: rgba(15, 23, 42, 0.95); border: 1px solid #a855f7; border-radius: 12px; padding: 30px; max-width: 600px; width: 100%; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.8); }
        h1 { color: #a855f7; font-size: 20px; }
        a { color: #38bdf8; text-decoration: none; display: inline-block; margin-top: 20px; font-weight: bold; background: #1e293b; padding: 10px 15px; border-radius: 6px; border: 1px solid #38bdf8; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🕹️ Fast Decision & NPC Game</h1>
        <p style="color: #10b981;">Interactive Decision-Making & Autonomous Behavioral Simulation Active</p>
        <a href="index.html">← Back to Dashboard Hub</a>
    </div>
</body>
</html>""")

# 5. Synth
with open("synth.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vyom Wave Synthesizer</title>
    <style>
        body { background: #030712; color: #f3f4f6; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        .synth-box { background: rgba(15, 23, 42, 0.95); border: 1px solid #38bdf8; border-radius: 12px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); text-align: center; max-width: 500px; width: 100%; }
        h1 { color: #38bdf8; font-size: 18px; margin-top: 0; }
        .control-group { margin: 12px 0; text-align: left; }
        label { display: block; margin-bottom: 5px; color: #a855f7; font-weight: bold; font-size: 12px; }
        input[type=range], select { width: 100%; accent-color: #38bdf8; background: #1e293b; color: #38bdf8; border: 1px solid #38bdf8; padding: 8px; border-radius: 6px; font-family: monospace; box-sizing: border-box; }
        button { background: #38bdf8; color: #030712; border: none; padding: 12px; font-weight: bold; border-radius: 6px; cursor: pointer; font-family: monospace; font-size: 13px; width: 100%; margin-top: 8px; }
        .keys { display: flex; justify-content: center; gap: 5px; margin-top: 12px; }
        .key { background: #1e293b; border: 1px solid #38bdf8; color: #38bdf8; padding: 12px 6px; cursor: pointer; border-radius: 6px; font-weight: bold; flex: 1; text-align: center; font-size: 12px; }
        .back-link { display: block; margin-top: 15px; color: #38bdf8; text-decoration: none; font-size: 12px; font-weight: bold; background: #1e293b; padding: 10px; border-radius: 6px; border: 1px solid #38bdf8; text-align: center; }
    </style>
</head>
<body>
    <div class="synth-box">
        <h1>🎛️ Vyom Wave Synthesizer</h1>
        <div class="control-group">
            <label>Frequency (Hz): <span id="freq-val">440</span> Hz</label>
            <input type="range" id="freqRange" min="100" max="1000" value="440" oninput="updateFreq(this.value)">
        </div>
        <div class="control-group">
            <label>Waveform</label>
            <select id="waveType">
                <option value="sine">Sine Wave</option>
                <option value="square">Square Wave</option>
                <option value="sawtooth">Sawtooth Wave</option>
                <option value="triangle">Triangle Wave</option>
            </select>
        </div>
        <button onclick="toggleSound()" id="playBtn">▶ Start Synth Engine</button>
        <div class="keys">
            <div class="key" onclick="playNote(261.63)">C4</div>
            <div class="key" onclick="playNote(293.66)">D4</div>
            <div class="key" onclick="playNote(329.63)">E4</div>
            <div class="key" onclick="playNote(349.23)">F4</div>
            <div class="key" onclick="playNote(392.00)">G4</div>
        </div>
        <a href="index.html" class="back-link">← Back to Dashboard Hub</a>
    </div>
    <script>
        let audioCtx = null, osc = null, gainNode = null, isPlaying = false;
        function initAudio() { if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }
        function toggleSound() {
            initAudio();
            const btn = document.getElementById("playBtn");
            if (!isPlaying) {
                if (audioCtx.state === "suspended") audioCtx.resume();
                osc = audioCtx.createOscillator();
                gainNode = audioCtx.createGain();
                osc.type = document.getElementById("waveType").value;
                osc.frequency.setValueAtTime(parseFloat(document.getElementById("freqRange").value), audioCtx.currentTime);
                gainNode.gain.setValueAtTime(0.15, audioCtx.currentTime);
                osc.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                osc.start();
                isPlaying = true;
                btn.innerText = "⏹ Stop Synth Engine";
                btn.style.background = "#ef4444";
            } else {
                if (osc) { osc.stop(); osc.disconnect(); }
                isPlaying = false;
                btn.innerText = "▶ Start Synth Engine";
                btn.style.background = "#38bdf8";
            }
        }
        function updateFreq(val) {
            document.getElementById("freq-val").innerText = val;
            if (isPlaying && osc) osc.frequency.setValueAtTime(parseFloat(val), audioCtx.currentTime);
        }
        function playNote(freq) {
            initAudio();
            if (audioCtx.state === "suspended") audioCtx.resume();
            let tempOsc = audioCtx.createOscillator();
            let tempGain = audioCtx.createGain();
            tempOsc.type = document.getElementById("waveType").value;
            tempOsc.frequency.setValueAtTime(freq, audioCtx.currentTime);
            tempGain.gain.setValueAtTime(0.2, audioCtx.currentTime);
            tempGain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.8);
            tempOsc.connect(tempGain);
            tempGain.connect(audioCtx.destination);
            tempOsc.start();
            tempOsc.stop(audioCtx.currentTime + 0.8);
        }
    </script>
</body>
</html>""")

# 6. Badminton
with open("badminton.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Badminton Physics Simulation</title>
    <style>
        body { background: #030712; color: #f3f4f6; font-family: monospace; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        h1 { color: #38bdf8; margin: 5px; font-size: 18px; text-align: center; }
        canvas { background: #0f172a; border: 2px solid #38bdf8; border-radius: 8px; width: 100%; max-width: 600px; height: auto; display: block; }
        .score { font-size: 13px; color: #10b981; margin-bottom: 8px; font-weight: bold; text-align: center; }
        .back-link { display: block; margin-top: 15px; color: #38bdf8; text-decoration: none; font-size: 12px; font-weight: bold; background: #1e293b; padding: 10px; border-radius: 6px; border: 1px solid #38bdf8; text-align: center; max-width: 600px; box-sizing: border-box; }
    </style>
</head>
<body>
    <h1>🏸 Badminton Physics Simulation</h1>
    <div class="score">Score: <span id="scoreVal">0</span> | Touch/Move up-down to play</div>
    <canvas id="gameCanvas" width="600" height="250"></canvas>
    <a href="index.html" class="back-link">← Back to Dashboard Hub</a>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        let score = 0;
        let shuttle = { x: 60, y: 125, vx: 3.5, vy: 2, radius: 7 };
        let racket = { x: 570, y: 100, width: 12, height: 60 };

        canvas.addEventListener("mousemove", (e) => {
            const rect = canvas.getBoundingClientRect();
            racket.y = (e.clientY - rect.top) * (canvas.height / rect.height) - racket.height / 2;
        });
        canvas.addEventListener("touchmove", (e) => {
            const rect = canvas.getBoundingClientRect();
            if(e.touches.length > 0) {
                racket.y = (e.touches[0].clientY - rect.top) * (canvas.height / rect.height) - racket.height / 2;
            }
            e.preventDefault();
        }, {passive: false});

        function updateGame() {
            shuttle.x += shuttle.vx;
            shuttle.y += shuttle.vy;
            shuttle.vy += 0.07;

            if (shuttle.y < 10) { shuttle.y = 10; shuttle.vy *= -1; }
            if (shuttle.y > canvas.height - 10) { shuttle.y = canvas.height - 10; shuttle.vy *= -1; }
            if (shuttle.x < 10) { shuttle.x = 10; shuttle.vx *= -1; }

            if (
                shuttle.x >= racket.x &&
                shuttle.x <= racket.x + racket.width &&
                shuttle.y >= racket.y &&
                shuttle.y <= racket.y + racket.height
            ) {
                shuttle.vx *= -1.08;
                shuttle.vy += (Math.random() - 0.5) * 3;
                score++;
                document.getElementById("scoreVal").innerText = score;
            }

            if (shuttle.x > canvas.width) {
                score = 0;
                document.getElementById("scoreVal").innerText = score;
                shuttle.x = 60; shuttle.y = 125; shuttle.vx = 3.5; shuttle.vy = 2;
            }
        }

        function drawGame() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.strokeStyle = "#38bdf8"; ctx.setLineDash([4, 4]);
            ctx.beginPath(); ctx.moveTo(canvas.width / 2, 0); ctx.lineTo(canvas.width / 2, canvas.height); ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(shuttle.x, shuttle.y, shuttle.radius, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = "#a855f7"; ctx.fillRect(racket.x, racket.y, racket.width, racket.height);
        }

        function gameLoop() { updateGame(); drawGame(); requestAnimationFrame(gameLoop); }
        gameLoop();
    </script>
</body>
</html>""")

# 7. README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write("""<div align="center">

# 🚀 Vyom Sutra (व्योम सूत्र)
### *Ultra-Fast Wave-Based Decision, Signal Processing & Simulation Engine*

[![PyPI version](https://img.shields.io/pypi/v/vyom-sutra.svg?color=blue&style=for-the-badge)](https://pypi.org/project/vyom-sutra/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg?style=for-the-badge)](https://www.python.org/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22247703-blueviolet.svg?style=for-the-badge)](https://doi.org/10.5281/zenodo.22247703)

<br />

[🚨 **Disaster Prediction**](https://pogtvt.github.io/Vyom_sutra/Disaster_prediction/Disaster_prediction.html) • [🌌 **Universe Sim**](https://pogtvt.github.io/Vyom_sutra/universe_simulation.html) • [🕹️ **NPC Game**](https://pogtvt.github.io/Vyom_sutra/fast_decision_npc_game.html) • [🎛️ **Synthesizer**](https://pogtvt.github.io/Vyom_sutra/synth.html) • [🏸 **Badminton Game**](https://pogtvt.github.io/Vyom_sutra/badminton.html) • [🎮 **Master Hub**](https://pogtvt.github.io/Vyom_sutra/index.html)

</div>

---

## ⚡ Overview

**Vyom Sutra** is a high-performance, wave-based similarity and signal processing engine designed with **Sine-Wave Universality** and **Null-Infinite Duality ($0 = \infty$)**.

---

## 🚨 1. Critical Early-Warning Systems (Highest Priority)

* 🚀 **[Disaster Prediction System](https://pogtvt.github.io/Vyom_sutra/Disaster_prediction/Disaster_prediction.html)**
  *Critical early-warning prediction system powered by wave mechanics and real-time risk evaluation.*

---

## 🌌 2. Core Simulations & Games (High Priority)

* 🚀 **[Universe Simulation Engine](https://pogtvt.github.io/Vyom_sutra/universe_simulation.html)**
  *Universal scale-summation and cosmic field wave simulation engine.*

* 🚀 **[Fast Decision & NPC Game](https://pogtvt.github.io/Vyom_sutra/fast_decision_npc_game.html)**
  *Interactive decision-making and autonomous NPC behavioral game simulation module.*

---

## 🎛️ 3. Synthesizers & Physics Games (Interactive)

* 🚀 **[Vyom Wave Synthesizer](https://pogtvt.github.io/Vyom_sutra/synth.html)**
  *Web Audio API-driven signal generator with frequency sliders, waveforms, and live musical keys.*

* 🚀 **[Badminton Physics Simulation Game](https://pogtvt.github.io/Vyom_sutra/badminton.html)**
  *Real-time canvas physics engine calculating gravity vectors and shuttlecock-racket collisions with full touch/mouse support.*

* 🚀 **[Master Dashboard Hub](https://pogtvt.github.io/Vyom_sutra/index.html)**
  *Central dashboard hub connecting all active modules.*

---

## 📦 Quick Start & Installation

```bash
pip install vyom-sutra
```""")

print("SUCCESS: All files and README links created successfully!")
