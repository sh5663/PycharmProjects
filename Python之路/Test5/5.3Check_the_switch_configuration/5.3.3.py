#coding utf-8
import paramiko
import time
import socket

username = input('Enter username: ')
password = input('Enter password: ')

switch_auth_issce = []
switch_unreachable = []

f = open(r'D:\PycharmProjects\Python之路\4实验\test2批量登陆不同网段的SW\ip_list.txt', 'r')
for line in f.readlines():
    try:
        iplist = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=iplist,username=username,password=password,look_for_keys=False)
        print('You have successfully connet switch ' + iplist)
        command = ssh_client.invoke_shell()
        command.send('reload\n')
        command.send('\n')
        time.sleep(2)
        output = command.recv(65535)
        print(output.decode('ascii'))
    except paramiko.ssh_exception.AuthenticationException:
        print('认证错误 '+ iplist)
        switch_auth_issce.append(iplist)
    except socket.error:
        print('IP '+iplist+' 不可达')
        switch_unreachable.append(iplist)
    f.close()
    ssh_client.close()