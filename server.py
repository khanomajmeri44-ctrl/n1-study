#!/usr/bin/env python3
"""Static file server with cache-busting headers — no Ctrl+Shift+R needed."""

import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
NO_CACHE_EXTENSIONS = {'.html', '.js', '.css'}

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Determine the actual file being served
        path = self.path.split('?')[0]  # strip query params
        # Directory paths serve index.html; treat them as .html
        if path.endswith('/') or path == '':
            effective = '.html'
        else:
            effective = path
        if any(effective.endswith(ext) for ext in NO_CACHE_EXTENSIONS):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        elif any(effective.endswith(ext) for ext in ('.png', '.jpg', '.svg', '.woff', '.ttf')):
            self.send_header('Cache-Control', 'public, max-age=86400')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for directory requests
        path = self.path.split('?')[0]
        if path.endswith('/'):
            index = os.path.join(self.directory or '.', path.lstrip('/'), 'index.html')
            if os.path.isfile(index):
                self.path = path
        super().do_GET()

    def log_message(self, format, *args):
        # Quiet logging
        pass

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or '.')
    with http.server.HTTPServer(('0.0.0.0', PORT), NoCacheHandler) as httpd:
        print(f'🚀 Serving at http://0.0.0.0:{PORT} (no-cache on HTML/JS/CSS)')
        httpd.serve_forever()
