# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

hostName = "0.0.0.0"
serverPort = 10000

current_time = datetime.now().strftime("%M:%H %d/%m/%Y")
current_time_print_msg = "<p>Today is" + current_time + "</p>"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is a test web server</p>", "utf-8"))
        self.wfile.write(bytes(current_time_print_msg, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        webServer.server_close()
        print("Server stopped")

