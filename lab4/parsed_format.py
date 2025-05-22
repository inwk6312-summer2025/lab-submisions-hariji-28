from netmiko import Netmiko
device = {"device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22"}
net_connect = Netmiko(**device)
output = net_connect.send_command("show ip interface brief", use_textfsm=True)
net_connect.disconnect()
print(type(output))
for interface in output:
 print(interface['interface'])
