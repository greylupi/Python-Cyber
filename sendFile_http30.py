#for this script to work a file needs to be present in the folder. For this example i created dummy.txt

import urllib
import requests
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]
#headers = {'Content-Type': 'multipart/form-data'}
files = {'filename': ('../dummy.txt', open('dummy.txt','rb'))}

response = requests.get(host, files=files)

print(response.text)