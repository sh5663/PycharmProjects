from netmiko import ConnectHandler
import json

SW1 = {
    'device_type':'cisco_ios',
    'ip':'203.0.113.1',
    'username':'qytang',
    'password':'qytang',
}
connect = ConnectHandler(**SW1)
print('Successfully connnect to '+SW1['ip'])
interface = connect.send_command('show ip int br',use_textfsm=True)
for interface in interface:
    if interface['status']=='up':
        print(f'{interface["intf"]} is up! IP address:{interface["ipaddr"]}')
# print(json.dumps(interface,indent=2))