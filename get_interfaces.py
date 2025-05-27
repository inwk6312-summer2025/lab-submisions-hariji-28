import logging
import requests
from requests.auth import HTTPBasicAuth
import json
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)
def get_interfaces(append_url):
 url = BASE_URL + append_url
 auth = HTTPBasicAuth(USER, PASS)
 headers = {'Accept': 'application/vnd.yang.data+json'}
 logging.info(f"URL ==> {url}")
 response = requests.get(url, auth=auth, headers=headers)
 if response.status_code == 200:
  logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
  return json.dumps(response.json(), sort_keys=True, indent=4 )
 else:
  logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
  return response.text
print(get_interfaces('interfaces'))
