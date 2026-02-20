#!/usr/bin/python3
"""
Advanced Simple API using Python's http.server module with logging
"""


import http.server
import socketserver
import json
from datetime import datetime


class AdvancedAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Advanced HTTP request handler with logging
    """

    def log_message(self, format, *args):
        """
        Custom log message format
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {self.address_string()} - {format % args}")

    def do_GET(self):
        """
        Handle GET requests
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
                "endpoints": [
                    "/",
                    "/data",
                    "/status",
                    "/info"
                ]
            }
            self.wfile.write(json.dumps(info, indent=2).encode())

        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {
                "error": "Endpoint not found",
                "path": self.path
            }
            self.wfile.write(json.dumps(error).encode())


def run(port=8000):
    """
    Run the HTTP server
    """
    server_address = ('', port)
    httpd = socketserver.TCPServer(server_address, AdvancedAPIHandler)
    print(f"Server running on port {port}...")
    print(f"Access: http://localhost:{port}/")
    print("Press Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.shutdown()


if __name__ == "__main__":
    run()
