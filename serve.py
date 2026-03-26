#!/usr/bin/env python3
"""Simple HTTP server for the MGRS map application on port 8001."""

import http.server
import os

PORT = 8001

os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
