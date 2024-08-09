import socket

IP = "127.0.0.1"
PORT = 5000
CHUNK_SIZE = 1024
MESSAGE = b"Hello!"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((IP, PORT))
    print(f"Server started on {IP}:{PORT}")
    for _ in range(10):
        data, addr = sock.recvfrom(1024)
        print("Ping Received")
        sock.sendto(MESSAGE, addr)