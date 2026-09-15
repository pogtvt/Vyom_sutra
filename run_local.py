#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("=" * 60)
    print(f"🚀 Vyom Sutra Local Server running at http://localhost:{PORT}")
    print("👉 Open http://localhost:8000/index.html in your browser!")
    print("Press Ctrl+C to stop the server.")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
