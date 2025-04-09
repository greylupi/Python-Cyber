import sys
import argparse
from websocket import create_connection

parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]

ws = create_connection("ws://" + host)
ws.send("key")
print(ws.recv())