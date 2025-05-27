import logging
import requests
from requests.auth import HTTPBasicAuth
import json
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)
def set_interfaces(append_url, interface_name):
 url = BASE_URL + append_url + interface_name
 auth = HTTPBasicAuth(USER, PASS)
 headers = {
 'Accept': 'application/vnd.yang.data+json',
 'Content-Type': 'application/vnd.yang.data+json'
 }
 data = {
  "ietf-interfaces:interface": {
  "name": "GigabitEthernet3",
  "description": "Changed through Restconf",
  "type": "iana-if-type:ethernetCsmacd",
  "enabled": 'true',
  "ietf-ip:ipv4": {
   "address": [
   {
    "ip": "10.0.10.3",
    "netmask": "255.255.255.0"
   }
  ]
 },
 "ietf-ip:ipv6": {}
 }
 }
 response = requests.put(url, auth=auth, headers=headers,
data=json.dumps(data))
 if response.status_code == 204:
  logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
  return "success!"
 else:
  logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
  return response.text
print (set_interfaces("interfaces/interface/", "GigabitEthernet3"))

