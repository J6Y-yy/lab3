import socket
import threading

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
    print(f"Client disconnected: {addr}")
    conn.close()

def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        print(f"Server started on port {port}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr))
            t.start()

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1])
    start_server(port)

