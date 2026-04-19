from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import time
import requests


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

            response = f"<h2>Hello, {name}!</h2>"
            self.wfile.write(response.encode())


def run_server():
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Server started")

    def stop_server():
        time.sleep(5)
        server.shutdown()

    threading.Thread(target=stop_server).start()
    server.serve_forever()


def test_server():
    time.sleep(1)
    try:
        res = requests.get("http://localhost:8000")
        print("Test Status Code:", res.status_code)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    run_server()
    test_server()
