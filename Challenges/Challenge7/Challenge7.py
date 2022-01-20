import os
import requests
import json
requests.packages.urllib3.disable_warnings()

IP ="192.168.56.101"
os.system("ping -c 5 "+IP) 
INTERFACE="GigabitEthernet1"
USER = "cisco"
PSW = "Cisco123!"
URL = "https://" + IP + "/restconf/data/ietf-interfaces:interfaces/interface=" + INTERFACE
HEADER = {"Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"}
AUTH = (USER, PSW)
status = requests.get(URL, auth=AUTH, headers=HEADER, verify=False)
status_code = str(status.status_code)

print(status_code)

if ( status_code == 200 ): 
   print ("Yes - interface is up - returning status code: 200")
else:
   print ("No - interface is down - returning status code:" + status_code)