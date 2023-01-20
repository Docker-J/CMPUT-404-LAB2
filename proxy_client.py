import socket

host = "127.0.0.1"
port = 8001
buffer_size = 1024
payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote_ip = socket.gethostbyname(host)
s.connect((remote_ip, port))
s.sendall(payload.encode())
s.shutdown(socket.SHUT_WR)

full_data = s.recv(buffer_size)
print(full_data)

s.close()