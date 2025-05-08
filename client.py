import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server> <port> <file>")
        return
    
    server, port, filepath = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, port))
            print(f"Connected to server at {server}:{port}")
    except Exception as e:
        print(f"Connection error: {e}")
        return

if __name__ == "__main__":
    main()
