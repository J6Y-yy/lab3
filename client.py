import socket
import sys
import re

def parse_requests(filepath):
    requests = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(' ', 2)
            if len(parts) < 3:
                print(f"Invalid request: {line}")
                continue
            cmd, key, value = parts
            if cmd == 'PUT':
                requests.append((cmd, key, value))
            
    return requests

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server> <port> <file>")
        return
    
    server, port, filepath = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    requests = parse_requests(filepath)
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, port))
            print(f"Connected to server at {server}:{port}")
            for req in requests:
                cmd, key, value = req
           
    except Exception as e:
        print(f"Connection error: {e}")
        return

if __name__ == "__main__":
    main()
