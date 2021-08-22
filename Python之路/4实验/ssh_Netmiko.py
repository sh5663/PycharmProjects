from netmiko import ConnectHandler
SW2 = {
    'device_type':'cisco_ios',
    'ip':'203.0.113.2',
    'username':'qytang',
    'password':'qytang'
}
connect = ConnectHandler(**SW2)
print('Successfuly connected to  '+SW2['ip'])
config_commands = ['int loo 1 ','ip add 2.2.2.2 255.255.255.255']
output = connect.send_config_set(config_commands)
print(output)
result = connect.send_command('show run int  loo 1')
print(result)