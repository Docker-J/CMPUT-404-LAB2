import socket
from multiprocessing import Process

host = ""
port = 8001
buffer_size = 1024

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(2)

    while True:
        conn, addr = s.accept()
        p = Process(target=handle_echo, args=(addr, conn))
        p.daemon = True
        p.start()

def handle_echo(addr, conn):
    full_data = conn.recv(buffer_size)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()