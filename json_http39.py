import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()


host = sys.argv[1]
headers = {'Content-Type': 'application/json'}
data = "{\"key\":\"please\\\"\"}"

response = requests.post(host, headers=headers, data=data)

print(response.text)