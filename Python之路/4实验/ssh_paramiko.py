import paramiko
import time
ip = '203.0.113.1'
usname = 'qytang'
paword = 'qytang'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=usname,password=paword, allow_agent=False,look_for_keys=False )

print('Successfully connected to ',ip)

command = ssh_client.invoke_shell()
command.send('config t\n')
command.send('int loo 1 \n')
command.send('ip add 1.1.1.1 255.255.255.255\n')
command.send('end\n')
command.send('wr \n')
time.sleep(2)
output = command.recv(65535)
print(output.decode('ascii'))

ssh_client.close()

