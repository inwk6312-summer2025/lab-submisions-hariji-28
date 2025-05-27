import yaml
import requests
import json
from requests.auth import HTTPBasicAuth
import logging

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

USER = 'student'
PASS = 'Meilab123'

HEADERS = {
    'Accept': 'application/vnd.yang.data+json',
    'Content-Type': 'application/vnd.yang.data+json'
}

with open('router_interfaces.yaml') as file:
    config = yaml.safe_load(file)

def configure_interface(router_ip, interface_name, ip_address, netmask):
    base_url = f"http://{router_ip}/restconf/api/running/"
    url = base_url + f"interfaces/interface/GigabitEthernet{interface_name.replace('G0/', '')}"
    
    data = {
        "ietf-interfaces:interface": {
            "name": f"GigabitEthernet{interface_name.replace('G0/', '')}",
            "description": f"Configured by RESTCONF",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": 'true',
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip_address,
                        "netmask": netmask
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }

    response = requests.put(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=HEADERS, data=json.dumps(data))

    if response.status_code == 204:
        logging.info(f"Configured {interface_name} on {router_ip}")
    else:
        logging.error(f"Failed to configure {interface_name} on {router_ip}: {response.status_code} - {response.text}")

for router in config['routers']:
    mgmt_ip = router['management_ip']
    interfaces = router['interfaces']
    for intf_name, intf_data in interfaces.items():
        configure_interface(mgmt_ip, intf_name, intf_data['ip'], intf_data['netmask'])
