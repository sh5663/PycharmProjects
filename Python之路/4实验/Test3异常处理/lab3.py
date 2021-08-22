import paramiko
import time
import sys
import socket


username = input('username: ')
password = input('password: ')
ip_file = sys.argv[0]
cmd_file = sys.argv[0]

switch_with_authentication_issue = []
switch_not_reachable = []

iplist = open(r'D:\PycharmProjects\Python之路\4实验\test2批量登陆不同网段的SW\ip_list.txt', 'r')

for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip,username=username,password=password,look_for_keys=False)
        print('You have successfully connect to ',ip)
        command = ssh_client.invoke_shell()
        cmdlist = open(r'D:\PycharmProjects\Python之路\4实验\Test3异常处理\cmd.txt','r')
        cmdlist.seek(0)
        for line in cmdlist.readlines():
            command.send(line + '\n')
        time.sleep(2)
        cmdlist.close()
        output = command.recv(65535)
        print(output.decode('ascii'))
    except paramiko.ssh_exception.AuthenticationException:
        print('User authentication failed for '+ ip + '.')
        switch_with_authentication_issue.append(ip)
    except socket.error:
        print(ip + ' is not reachable')
        switch_not_reachable.append(ip)
    iplist.close()
    ssh_client.close()


print('\nUser autehenticatiopn failed for below switches: ')
for i in switch_with_authentication_issue:
        flie = open(r'D:\PycharmProjects\Python之路\4实验\Test3异常处理\IPlist1.txt', 'a+')
        flie.write('User autehenticatiopn failed for below switches:'+i+'\n')
        flie.close()
        print(i)

print('\nBelow switches are not reachable: ')
for i in switch_not_reachable:
        flie = open(r'D:\PycharmProjects\Python之路\4实验\Test3异常处理\IPlist1.txt', 'a+')
        flie.write('Below switches are not reachable:'+i+'\n')
        flie.close()
        print(i)
