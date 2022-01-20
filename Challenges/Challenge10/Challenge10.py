import json
import requests

ipHosts = "192.168.56.101"
username = "cisco"
password = "cisco123!"

url = f"https://{ipHosts}:443/restconf/data/Cisco-IOS-XE-native/logging/monitor/severity"
statuscode=url
basicauth = (username, password)

headers = {"Accept": "application/yang-data+json", "Content-type": "application/yang-data+json"}

response = requests.options(url, auth=basicauth, headers=headers, verify=False)

print(statuscode)

for k, v in response.headers.items():
    print(f"{k}: {v}")

print(response.raw.version)
