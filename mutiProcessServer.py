import socket
import os
import time
from concurrent.futures import ProcessPoolExecutor


# 处理客户端请求
def handle_client(client_socket):
    print(os.getpid())
    request = client_socket.recv(1024).decode('utf-8')
    # print(f"Received request: {request}")

    # 解析请求行
    request_line = request.splitlines()[0]
    request_method, path, _ = request_line.split()

    if path == '/' or path == '/index':
        serve_file(client_socket, 'index.html')
    elif path == '/sleep':
        handle_sleep(client_socket)
    else:
        send_response(client_socket, 404, "Page Not Found")

    client_socket.close()


# 发送文件内容作为响应
def serve_file(client_socket, filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            send_response(client_socket, 200, content)
    else:
        send_response(client_socket, 404, "File Not Found")


# 处理 /sleep 请求
def handle_sleep(client_socket):
    time.sleep(10)
    serve_file(client_socket, 'sleep.html')


# 发送响应
# 发送响应
def send_response(client_socket, status_code, content):
    status_messages = {200: "OK", 404: "Not Found"}
    response = f"HTTP/1.1 {status_code} {status_messages.get(status_code, '')}\r\n"
    response += "Content-Type: text/html\r\n"
    response += "Content-Length: {}\r\n".format(len(content.encode('utf-8')))
    response += "\r\n"
    response += content
    client_socket.sendall(response.encode('utf-8'))


# 启动服务器
def run_server(host='0.0.0.0', port=8000, max_workers=4):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Starting server on {host}:{port}...")

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            executor.submit(handle_client, client_socket)


if __name__ == '__main__':
    run_server()
