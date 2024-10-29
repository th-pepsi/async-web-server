import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.handle_request())

    async def handle_request(self):
        if self.path == '/' or self.path == '/index':
            response = await self.serve_file('index.html')
        elif self.path == '/sleep':
            response = await self.sleep_and_serve()
        else:
            self.send_error(404, "Page Not Found")
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response)

    async def serve_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content.encode('utf-8')
        else:
            self.send_error(404, "File Not Found")
            return b''

    async def sleep_and_serve(self):
        await asyncio.sleep(10)  # 异步等待 10 秒
        return await self.serve_file('sleep.html')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
