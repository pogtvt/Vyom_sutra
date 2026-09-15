<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vyom Sutra: Infinite Wave Badminton Rally</title>
    <style>
        body { 
            margin: 0; 
            background: #030712; 
            color: #f8fafc; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            min-height: 100vh; 
            overflow: hidden; 
        }
        .container { 
            width: 92%; 
            max-width: 850px; 
            background: #0b0f19; 
            border: 2px solid #1e293b; 
            border-radius: 14px; 
            box-shadow: 0 0 50px rgba(56, 189, 248, 0.15); 
            padding: 20px; 
            text-align: center;
        }
        h1 { 
            font-size: 19px; 
            color: #38bdf8; 
            margin-bottom: 4px; 
        }
        .subtitle { 
            font-size: 11px; 
            color: #94a3b8; 
            margin-bottom: 15px; 
        }
        canvas { 
            width: 100%; 
            height: 380px; 
            background: linear-gradient(to bottom, #0f172a, #030712); 
            border-radius: 10px; 
            border: 1px solid #1f2937; 
            display: block; 
            box-shadow: inset 0 0 30px rgba(0,0,0,0.8); 
        }
        .telemetry {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 15px;
        }
        .tele-card {
            background: #111827;
            border: 1px solid #1f2937;
            padding: 10px;
            border-radius: 8px;
            font-size: 12px;
        }
        .tele-card span { color: #94a3b8; display: block; margin-bottom: 4px; }
        .tele-card strong { color: #38bdf8; font-size: 14px; }
    </style>
</head>
<body>
<div class="container">
    <h1>Vyom Sutra: Infinite Wave Badminton Engine</h1>
    <div class="subtitle">Powered by Null-Infinite Duality & Continuous Sine-Wave Mechanics ($0 = \infty$)</div>

    <canvas id="gameCanvas" width="800" height="400"></canvas>

    <div class="telemetry">
        <div class="tele-card">
            <span>RALLY COUNT (INFINITE)</span>
            <strong id="rallyVal">0</strong>
        </div>
        <div class="tele-card">
            <span>VYOM SIMILARITY SCORE</span>
            <strong id="scoreVal">100.00</strong>
        </div>
        <div class="tele-card">
            <span>WAVE COSMIC STATE</span>
            <strong id="stateVal">Harmonic</strong>
        </div>
    </div>
</div>

<script>
    // Vyom Engine Integration for Dynamic Wave Physics & Scoring
    class VyomEngine {
        constructor() {
            this.scale = 2.0;
        }

        calculateWaveState(amplitude) {
            let currentAmp = Math.max(0.05, Math.min(3.0, amplitude));
            let wavelength = Math.round(100 - ((currentAmp - 0.05) / 2.95) * 99);
            wavelength = Math.max(1, Math.min(100, wavelength));

            let cosmicState = "Harmonic";
            if (wavelength >= 98 || currentAmp <= 0.08) {
                cosmicState = "Real Zero / Infinity";
            } else if (currentAmp >= 2.6 && wavelength <= 5) {
                cosmicState = "Black Hole / Singularity";
            } else if (wavelength >= 70) {
                cosmicState = "Expanding Universe";
            }
            return { amplitude: currentAmp, wavelength, cosmicState };
        }

        getVyomScore(value, target = 1.0, scale = 2.0) {
            let theta = value % Math.PI;
            let d = Math.abs(target - theta);
            let score = Math.cos(d * scale) * 100.0;
            return Math.max(0, score);
        }
    }

    const vyom = new VyomEngine();
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    let shuttle = { x: 400, y: 150, vx: 4.5, vy: -2, gravity: 0.15 };
    let p1 = { x: 100, y: 280, width: 16, height: 70, color: '#38bdf8' };
    let p2 = { x: 684, y: 280, width: 16, height: 70, color: '#f43f5e' };
    let rallyCount = 0;
    let currentScore = 100;
    let currentState = "Harmonic";

    function updatePhysics() {
        // Continuous wave motion
        shuttle.vy += shuttle.gravity;
        shuttle.x += shuttle.vx;
        shuttle.y += shuttle.vy;

        // Autonomous smooth AI racket movements using wave functions
        if (shuttle.x < 400) {
            p1.y += ((shuttle.y + 15) - p1.y) * 0.1;
            p1.x = 100 + Math.sin(Date.now() * 0.003) * 30;
        } else {
            p1.y += (280 - p1.y) * 0.06;
        }

        if (shuttle.x >= 400) {
            p2.y += ((shuttle.y + 15) - p2.y) * 0.1;
            p2.x = 684 - Math.sin(Date.now() * 0.003) * 30;
        } else {
            p2.y += (280 - p2.y) * 0.06;
        }

        p1.y = Math.max(100, Math.min(310, p1.y));
        p2.y = Math.max(100, Math.min(310, p2.y));

        // Center net collision reflection
        if (shuttle.x > 392 && shuttle.x < 408 && shuttle.y > 220) {
            shuttle.vx *= -1;
            shuttle.vy = -6;
        }

        // INFINITE MODE: Ground hit triggers a Quantum Wave Rebound (Never Game Over!)
        if (shuttle.y >= 370) {
            shuttle.y = 370;
            shuttle.vy = -9.5; // Smooth upward bounce
            shuttle.vx *= 1.05; // Keep momentum flowing
            if(Math.abs(shuttle.vx) > 7) shuttle.vx = 5; // Limit extreme speed
            rallyCount++;
        }

        // Racket 1 Collision
        if (shuttle.x - 8 < p1.x + p1.width && shuttle.x + 8 > p1.x && shuttle.y - 8 < p1.y + p1.height && shuttle.y + 8 > p1.y) {
            shuttle.vx = Math.abs(shuttle.vx) + 0.2;
            shuttle.vy = -8.0 - Math.random() * 1.5;
            rallyCount++;
        }

        // Racket 2 Collision
        if (shuttle.x - 8 < p2.x + p2.width && shuttle.x + 8 > p2.x && shuttle.y - 8 < p2.y + p2.height && shuttle.y + 8 > p2.y) {
            shuttle.vx = -(Math.abs(shuttle.vx) + 0.2);
            shuttle.vy = -8.0 - Math.random() * 1.5;
            rallyCount++;
        }

        // Calculate Vyom Metrics dynamically based on shuttle velocity and position[span_2](start_span)[span_2](end_span)
        let waveData = vyom.calculateWaveState(Math.abs(shuttle.vy) * 0.3);
        currentScore = vyom.getVyomScore(shuttle.x * 0.01, 1.5, 1.8).toFixed(2);
        currentState = waveData.cosmicState;

        // Update UI telemetry
        document.getElementById('rallyVal').innerText = rallyCount;
        document.getElementById('scoreVal').innerText = currentScore;
        document.getElementById('stateVal').innerText = currentState;
    }

    function renderGraphics() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Background grid aesthetics
        ctx.strokeStyle = '#111827';
        ctx.lineWidth = 1;
        for(let i = 0; i < canvas.width; i += 50) {
            ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
        }

        // Court floor
        ctx.fillStyle = '#1e293b'; 
        ctx.fillRect(0, 370, canvas.width, 30);
        
        // Net
        ctx.fillStyle = '#cbd5e1'; 
        ctx.fillRect(397, 210, 6, 160);

        // Rackets
        ctx.fillStyle = p1.color; 
        ctx.fillRect(p1.x, p1.y, p1.width, p1.height);
        ctx.fillStyle = p2.color; 
        ctx.fillRect(p2.x, p2.y, p2.width, p2.height);

        // Shuttlecock with glowing effect
        ctx.beginPath(); 
        ctx.arc(shuttle.x, shuttle.y, 8, 0, Math.PI * 2); 
        ctx.fillStyle = '#facc15'; 
        ctx.shadowBlur = 15;
        ctx.shadowColor = '#facc15';
        ctx.fill(); 
        ctx.closePath();
        ctx.shadowBlur = 0;

        // On-screen overlay text
        ctx.fillStyle = '#f8fafc'; 
        ctx.font = 'bold 16px sans-serif'; 
        ctx.fillText('⚡ Vyom Infinite Rally: ' + rallyCount, 25, 35);
    }

    function gameLoop() { 
        updatePhysics(); 
        renderGraphics(); 
        requestAnimationFrame(gameLoop); 
    }
    gameLoop();
</script>
</body>
</html>
