import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True,
autoescape=True)
template = env.get_template('interfaces_config_template.j2')
loopback_config = template.render(data=interfaces)

for host in hosts["hosts"]:
 net_connect = Netmiko(host = host["name"],
    username = host["username"],
    password = host["password"],
    port = host["port"],
    device_type = host["type"])
 print(f"Logged into {host['name']} successfully")
 output = net_connect.send_config_set(loopback_config.split("\n"))
 print(f"Pushed config into {host['name']} successfully")
 net_connect.disconnect()
print("Done!")
