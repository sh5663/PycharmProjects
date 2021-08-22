import paramiko
import time
import re
from datetime import datetime
import  socket
username = input('Enter your SSH username: ')
password = input('Enter your SSH password:')
now = datetime.now()
date = '%s-%s-%s'%(now.month,now.day,now.year)
time_now = '%s-%s-%s'%(now.hour,now.minute,now.second)

switch_with_auth_issce = [] #认证错误
switch_unreachable = [] #IP不可达
total_number_of_up_port = 0 #端口UP数量
iplist = open(r'D:\PycharmProjects\Python之路\Test5\5.2Pythonping\reachable_ip.txt','r')
number_of_switch = len(iplist.readlines())  #交换机数量是IP列表的长度
total_number_of_ports = number_of_switch*7  #交换机端口数量=交换机*具体端口

iplist.seek(0)
for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_clinet = paramiko.SSHClient()
        ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_clinet.connect(hostname=ip,username=username,password=password,look_for_keys=False)
        print('\nYou have successfully connect to ',ip)

        command = ssh_clinet.invoke_shell()
        command.send('term len 0\n')
        command.send('show ip int br | in up \n')
        time.sleep(1)
        output = command.recv(65535)
        # print(output)
        search_up_port = re.findall(b'GigabitEthernet',output)  #在返回值中，匹配所有物理接口
        # GigabitEthernet为字符串，使用.encode()函数转换成字节型字符串
        number_of_up_switch = len(search_up_port)  #单台交换机UP端口的数量
        print(ip + ' has ' + str(number_of_up_switch)+' ports up.')
        total_number_of_up_port +=number_of_up_switch  #所有物理交换端口累加
    except paramiko.ssh_exception.AuthenticationException:
        print('TACACS is not working for '+ip+'.')
        switch_with_auth_issce.append(ip)
    except socket.error:
        print(ip + ' is not reachable.')
        switch_unreachable.append(ip)
iplist.close()
print('\n')
print('There are totally ' + str(total_number_of_ports)+' ports available in the network')
print(str(total_number_of_up_port)+' ports are currently up.')
print('Port up rate is %.2f%%'%(total_number_of_up_port/float(total_number_of_ports)*100))
print('\nTACACS is not working for below switches:')
for i in switch_with_auth_issce:
    print(i)
print('\nBelow switchs are not reachable:')
for i in switch_unreachable:
    print(i)
f = open('D:/PycharmProjects/Python之路/Test5/5.2Pythonping/'+date+'.txt','a+')
f.write('AS of ' + date+' ' + time_now)
f.write('\n\nThere are totally ' + str(total_number_of_ports)+' ports avaiable in the network.')
f.write('\n'+str(total_number_of_up_port)+' ports are currently up.')
f.write('\nPort up rate is %.2f%%'%(total_number_of_up_port/float(total_number_of_ports)*100))
f.write('\n'+'*'*60+'\n')
f.close()