from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("index.html", "r") as file:
                self.wfile.write(file.read().encode())

        elif self.path.startswith("/submit"):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)

            name = params.get("username", ["Guest"])[0]

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            response = f"""
            <html>
            <body>
                <h2>Hello, {name}! 👋</h2>
                <a href="/">Go Back</a>
            </body>
            </html>
            """

            self.wfile.write(response.encode())

        else:
            self.send_response(404)
            self.end_headers()


def run_server():
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()


# 👇 IMPORTANT CHANGE
if __name__ == "__main__":
    run_server()