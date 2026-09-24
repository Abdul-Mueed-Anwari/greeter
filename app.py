from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080
NAME = "Mueed"  

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
    f"<h1>hey, {NAME}!</h1>"
    f"<p>Keep shipping small wins.</p>"
).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(f"Serving on http://localhost:{PORT}")
    HTTPServer(("", PORT), Handler).serve_forever()