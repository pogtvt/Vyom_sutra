import os
import glob
import json

def build_ecosystem():
    # Find all HTML files except index.html
    html_files = [f for f in glob.glob("*.html") if os.path.isfile(f) and f != "index.html"]
    html_files.sort()

    cards_html = ""
    for f in html_files:
        name = f.replace(".html", "").replace("_", " ").title()
        cards_html += f'''
        <div class="module-card" data-name="{name.lower()}">
            <div class="card-header">
                <span class="badge">SIMULATION</span>
                <span class="status-dot">● ONLINE</span>
            </div>
            <h3>{name}</h3>
            <p>Interactive wave-based module governed by Master VyomEngine & 0 = ∞ duality.</p>
            <a href="{f}" class="launch-btn">🚀 Launch Module</a>
        </div>
        '''

    # 1 & 4. Master Index Hub with KaTeX & Canvas
    index_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vyom Sutra Ecosystem Hub</title>
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#030712">
    <!-- KaTeX for Scientific Equations -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>
    
    <style>
        :root {{
            --bg: #030712;
            --card-bg: rgba(15, 23, 42, 0.85);
            --border: #38bdf8;
            --text: #f3f4f6;
            --accent: #38bdf8;
            --purple: #a855f7;
        }}
        body {{
            background-color: var(--bg);
            color: var(--text);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }}
        canvas {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            pointer-events: none;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        header {{
            text-align: center;
            margin-bottom: 40px;
            border-bottom: 1px solid rgba(56, 189, 248, 0.3);
            padding-bottom: 30px;
        }}
        h1 {{
            font-size: 2.8rem;
            margin: 0 0 10px 0;
            background: linear-gradient(90deg, #38bdf8, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: monospace;
        }}
        .subtitle {{
            color: #94a3b8;
            font-size: 1.1rem;
        }}
        .search-box {{
            width: 100%;
            max-width: 500px;
            padding: 14px 20px;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid var(--border);
            border-radius: 12px;
            color: #fff;
            font-size: 1rem;
            margin: 0 auto 30px auto;
            display: block;
            outline: none;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 50px;
        }}
        .module-card {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(56, 189, 248, 0.4);
            border-radius: 16px;
            padding: 24px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 30px rgba(0,0,0,0.6);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .module-card:hover {{
            transform: translateY(-5px);
            border-color: var(--accent);
            box-shadow: 0 12px 40px rgba(56, 189, 248, 0.3);
        }}
        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            font-size: 0.75rem;
            font-family: monospace;
        }}
        .badge {{
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent);
            padding: 4px 8px;
            border-radius: 6px;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }}
        .status-dot {{
            color: #10b981;
        }}
        .module-card h3 {{
            margin: 0 0 10px 0;
            font-size: 1.3rem;
            color: #fff;
        }}
        .module-card p {{
            color: #94a3b8;
            font-size: 0.9rem;
            margin: 0 0 20px 0;
            line-height: 1.4;
        }}
        .launch-btn {{
            background: linear-gradient(135deg, #0284c7, #7c3aed);
            color: white;
            text-decoration: none;
            text-align: center;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 0.9rem;
            transition: opacity 0.2s;
        }}
        .launch-btn:hover {{
            opacity: 0.9;
        }}
        .paper-section {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border: 1px solid var(--purple);
            border-radius: 16px;
            padding: 30px;
            margin-top: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.7);
        }}
        .paper-section h2 {{
            color: var(--purple);
            font-family: monospace;
            margin-top: 0;
        }}
    </style>
</head>
<body>
    <canvas id="bgCanvas"></canvas>
    <div class="container">
        <header>
            <h1>🚀 Vyom Sutra Ecosystem Hub</h1>
            <p class="subtitle">Autonomous Wave-Based Computational Engine governed by $\text{Sine-Wave} = \text{Everything}$ & $0 = \infty$</p>
        </header>

        <input type="text" id="searchInput" class="search-box" placeholder="🔍 Search simulation modules..." onkeyup="filterModules()">

        <div class="grid" id="modulesGrid">
            {cards_html}
        </div>

        <div class="paper-section">
            <h2>📜 Theoretical Core: Vyom Sutra Principles</h2>
            <p>The universe operates as a continuous scale summation governed by null-infinite duality:</p>
            <p style="text-align: center; font-size: 1.2rem; margin: 20px 0;">
                $$\int_{0}^{\infty} \sin(\omega t + \phi) \, d\omega = 0 \iff \infty$$
            </p>
            <p>All simulation nodes, signal processors, and UI modules synchronize dynamically via Master VyomEngine.</p>
        </div>
    </div>

    <script>
        function filterModules() {{
            let input = document.getElementById('searchInput').value.toLowerCase();
            let cards = document.getElementsByClassName('module-card');
            for (let i = 0; i < cards.length; i++) {{
                let name = cards[i].getAttribute('data-name');
                if (name.includes(input)) {{
                    cards[i].style.display = "";
                }} else {{
                    cards[i].style.display = "none";
                }}
            }}
        }}

        const canvas = document.getElementById('bgCanvas');
        const ctx = canvas.getContext('2d');
        let width, height;
        function resize() {{
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }}
        window.addEventListener('resize', resize);
        resize();

        let particles = [];
        for(let i=0; i<60; i++) {{
            particles.push({{
                x: Math.random() * width,
                y: Math.random() * height,
                radius: Math.random() * 2 + 1,
                speedX: (Math.random() - 0.5) * 0.5,
                speedY: (Math.random() - 0.5) * 0.5
            }});
        }}

        let t = 0;
        function animate() {{
            ctx.fillStyle = 'rgba(3, 7, 18, 0.2)';
            ctx.fillRect(0, 0, width, height);

            ctx.beginPath();
            ctx.lineWidth = 1.5;
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
            for (let x = 0; x < width; x += 10) {{
                let y = height / 2 + Math.sin(x * 0.005 + t) * 100 * Math.sin(t * 0.5);
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }}
            ctx.stroke();

            ctx.fillStyle = 'rgba(168, 85, 247, 0.5)';
            particles.forEach(p => {{
                p.x += p.speedX;
                p.y += p.speedY;
                if (p.x < 0) p.x = width;
                if (p.x > width) p.x = 0;
                if (p.y < 0) p.y = height;
                if (p.y > height) p.y = 0;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fill();
            }});

            t += 0.03;
            requestAnimationFrame(animate);
        }}
        animate();
    </script>
</body>
</html>
'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)
    print("Master Index Hub generated successfully.")

    # 2. PWA Manifest
    manifest = {
        "name": "Vyom Sutra Ecosystem",
        "short_name": "VyomSutra",
        "start_url": "index.html",
        "display": "standalone",
        "background_color": "#030712",
        "theme_color": "#38bdf8",
        "icons": []
    }
    with open("manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)
    print("manifest.json generated.")

    # 3. Service Worker
    sw_code = """
    const CACHE_NAME = 'vyom-sutra-v1';
    const ASSETS = ['index.html'];

    self.addEventListener('install', (e) => {
        e.waitUntil(
            caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
        );
    });

    self.addEventListener('fetch', (e) => {
        e.respondWith(
            caches.match(e.request).then((response) => response || fetch(e.request))
        );
    });
    """
    with open("sw.js", "w", encoding="utf-8") as f:
        f.write(sw_code.strip())
    print("sw.js generated.")

if __name__ == "__main__":
    build_ecosystem()
