from http.server import BaseHTTPRequestHandler, HTTPServer

i = 0

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global i  # Declare i as global to modify it
        # Print a message when a request is received
        print(f"Received request from {self.client_address}")
        i += 1
        print(i)

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        self.wfile.write(b"Hello, world!")
        return

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
