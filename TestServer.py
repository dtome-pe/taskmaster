from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Literal


#Basic HTTP Server that simply responds client that it has received either a GET or a POST request

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Send 200 OK
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Hello, GET request received! Url->{self.headers["Host"]}{self.path}'.encode())

    def do_POST(self):
        self.send_response(200)  # Send 200 OK
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Hello, POST request received! Url->{self.headers["Host"]}{self.path}'.encode())

class TestServer:

    def __init__(self, port : int, server_class=HTTPServer, handler_class=SimpleHandler):
        server_address : tuple[Literal[''], int] = ('', port)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()