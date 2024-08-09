import socket
import time
from statistics import mean
from math import floor
from socket import error as SocketError
import errno

HOST = "127.0.0.1"
PORT = 5000
CHUNK_SIZE = 1024
MESSAGE = b"Hello!"


def print_times(rtt_list):
    if rtt_list:
        avg_rtt = mean(rtt_list) * 1000
        min_rtt = min(rtt_list) * 1000
        max_rtt = max(rtt_list) * 1000
        print(
            f"Approximate round trip times in milli-seconds:\n Minimum : {min_rtt:.5f}ms Maximum : {max_rtt:.5f}ms Average : {avg_rtt:.5f}ms")
    else:
        print("No data")


try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(1)
        # Send 10 udp ping messages
        rtt_times = []
        data_buf = None
        for i in range(10):
            try:
                sock.sendto(MESSAGE, (HOST, PORT))
                first_time = time.time()
                data_buf, addr = sock.recvfrom(1024)
                second_time = time.time()
                time_diff = second_time - first_time
                rtt_times.append(time_diff)

            except TimeoutError:
                print("Request timed out.")
                i -= 1
except SocketError as e:
    if e.errno == errno.ECONNRESET:
        print("Server not online!")
        exit(-1)
    else:
        raise
finally:
    sock.close()
    print_times(rtt_times)
