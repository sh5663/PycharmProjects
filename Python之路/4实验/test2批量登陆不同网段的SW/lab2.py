import paramiko
import time

username = input('username: ')
password = input('password: ')

f = open(r'D:\PycharmProjects\Python之路\4实验\test2批量登陆不同网段的SW\ip_list.txt', 'r')
for line in f.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)
    print('Successfully connext to ',ip)
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send('conf t\n')
    remote_connection.send('ip routing\n')
    remote_connection.send('router eigrp 1\n')
    remote_connection.send('end\n')
    remote_connection.send('wr\n')
    time.sleep(2)
    output = remote_connection.recv(65535)
    print(output.decode('ascii'))
    f.close()
    ssh_client.close()