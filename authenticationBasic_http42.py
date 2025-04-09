import requests
import sys
import argparse
from requests.auth import HTTPBasicAuth

parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]

auth = HTTPBasicAuth('key', 'please')

response = requests.get(host, auth=auth)

print(response.text)