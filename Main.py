'''Chat App Socket Programming'''

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")
except socket.error as err:
    print(f"Socket creation failed with error {err}")

    port = 80

    try:
        host_ip = socket.gethostbyname('www.github.com')
    except socket.gaierror:
        print("error resolving the host")
        sys.exit()