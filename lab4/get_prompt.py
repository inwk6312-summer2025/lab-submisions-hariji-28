from netmiko import Netmiko
device = {
 "device_type": "cisco_ios",
 "ip": "192.168.1.101", # Router 1
 "username": "student",
 "password": "Meilab123",
 "secret": "cisco",
 "port": "22",
}
net_connect = Netmiko(**device)
print(f"Default prompt: {net_connect.find_prompt()}")
net_connect.send_command_timing("disable")
print(f"Disable command: {net_connect.find_prompt()}")
net_connect.enable()
print(f"Enable command: {net_connect.find_prompt()}")
