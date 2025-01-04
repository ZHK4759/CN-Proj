import sys
import http.server
import socketserver
from http.server import ThreadingHTTPServer

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Needs one argument: server port")
        raise SystemExit

    PORT = int(sys.argv[1])

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # Suppress default logging

    with ThreadingHTTPServer(("", PORT), CustomHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"Server started at localhost:{PORT}")
        httpd.serve_forever()