import socket

host = "www.google.com"
port = 80
payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
buffer_size = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote_ip = socket.gethostbyname(host)
s.connect((remote_ip, port))
s.sendall(payload.encode())
s.shutdown(socket.SHUT_WR)

full_data = b""
while True:
    data = s.recv(buffer_size)
    if not data:
        break
    full_data += data
print(full_data)
s.close()