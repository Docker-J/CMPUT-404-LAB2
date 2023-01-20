import socket

host = ""
port = 8001
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(2)

while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    
    full_data = conn.recv(buffer_size)
    conn.sendall(full_data)
    conn.close()