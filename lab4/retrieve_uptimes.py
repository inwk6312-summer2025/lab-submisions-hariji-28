from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
            "ip": "192.168.1.101",
            "username": "student",
            "password": "Meilab123",
            "port": "22"},
            {"device_type": "cisco_ios",
            "ip": "192.168.1.102",
            "username": "student",
            "password": "Meilab123",
            "port": "22",
            }]
for device in devices:
 net_connect = Netmiko(**device)
 output = net_connect.send_command("show version")
 net_connect.disconnect()
 result = output.find('uptime is')
 begin = int(result)
 end = begin + 38
 print(device['ip'] + " => " + output[int(begin):int(end)])
