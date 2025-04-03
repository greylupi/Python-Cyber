# curl http://ptl-c8407dd0-20300804.libcurl.so/pentesterlab -X HACK

from urllib.request import Request, urlopen
import sys
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()
host = sys.argv[1]

httprequest = Request(host, method="HACK")
with urlopen(httprequest) as response:
    print(response.read().decode())
