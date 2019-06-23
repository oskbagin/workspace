import socket
import sys

try:
    HOST = sys.argv[1]
except IndexError:
    HOST = '127.0.0.1'
