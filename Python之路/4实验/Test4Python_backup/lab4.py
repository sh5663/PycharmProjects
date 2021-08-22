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
    command = ssh_client.invoke_shell()
    command.send('copy running-config tftp://203.0.113.60\n')
    time.sleep(5)
    output = command.recv(65535)
    print(output.decode('ascii'))
    f.close()
    ssh_client.close()