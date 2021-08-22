import  paramiko
import time
import getpass

username = input('Username: ')
password = input('Password: ')

for i in range(1,5):
    ip = '203.0.113.' + str(i)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)
    print('Successfully connect to ',ip)
    command = ssh_client.invoke_shell()
    command.send('conf t\n')
    for n in range(10,21):
        # print('Creating VLAN '+ str(n))
        print('Delnet VLAN ' + str(n))
        command.send(' vlan ' + str(n) + '\n')
        # command.send('name Python_VLAN ' + str(n) + '\n')
        time.sleep(2)
    command.send('end\n')
    command.send('wr\n')
    time.sleep(2)
    output = command.recv(65535)
    print(output.decode('ascii'))
    ssh_client.close()