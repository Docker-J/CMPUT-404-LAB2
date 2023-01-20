import socket
from multiprocessing import Process

host = ""
port = 8001
buffer_size = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((host, port))
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()
            p = Process(target=handle_proxy_end, args=(addr, conn))
            p.daemon = True
            p.start()

def handle_proxy_end(addr, conn):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
        remote_ip = socket.gethostbyname("www.google.com")
        proxy_end.connect((remote_ip, 80))
        
        send_full_data = conn.recv(buffer_size)
        proxy_end.sendall(send_full_data)

        proxy_end.shutdown(socket.SHUT_WR)

        data = proxy_end.recv(buffer_size)
        conn.send(data)
    
    conn.close()

if __name__ == "__main__":
    main()