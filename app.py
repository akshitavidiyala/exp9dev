from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker + Jenkins CI/CD!")

if __name__ == "__main__":
    print(f"Server running on port {PORT}")
    HTTPServer(("", PORT), Handler).serve_forever()

