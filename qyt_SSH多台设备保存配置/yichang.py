import paramiko
import time
import socket
from _datetime import datetime
date = datetime.now()
date1 = str(date)[0:16]
date1 = date1.replace(' ','_')
date1 =date1.replace(':','_')

# ip = '203.0.113.1';user = 'qytang';password = 'qytang'
devicelist = [
    {'device_name':'SW1','ip':'203.0.113.1','username':'qytang','password':'qytang','platfrom':'IOS'},
    {'device_name':'SW2','ip':'203.0.113.2','username':'qytang','password':'qytang','platfrom':'IOS'},
    {'device_name':'SW3','ip':'203.0.113.3','username':'qytang','password':'qytang','platfrom':'HW'},
    {'device_name':'SW4','ip':'203.0.113.4','username':'qytang','password':'qytang','platfrom':'HW'}
]

unreachable_list = []
auth_fail_list = []
def cisco(ipt,usernamet,passwordt):
    ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
    ssh1.connect(hostname=ipt,port=22,username=usernamet,password=passwordt,timeout=5,allow_agent=False,
                 look_for_keys=False) #allow_agent没有代理，look_for_keys不需要共享秘钥
    # time.sleep(15)  #测试使用

    cli = ssh1.invoke_shell()
    cli.send('terminal len 0\n')
    time.sleep(1)
    cli.send('show run\n')
    time.sleep(5)
    running  = cli.recv(99999).decode()
    # print(running)
    ssh1.close()
    return running

def huawei(ipt,usernamet,passwordt):
    ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
    ssh1.connect(hostname=ipt, port=22, username=usernamet, password=passwordt, timeout=5, allow_agent=False,
                 look_for_keys=False)
    # time.sleep(15)  #测试使用

    cli = ssh1.invoke_shell()
    cli.send('screen-length 0 temporary\n')
    time.sleep(1)
    # cli.send('sys\n')
    # time.sleep(1)
    cli.send('disp cu\n')
    time.sleep(5)
    running  = cli.recv(99999).decode()
    # print(running)
    ssh1.close()
    return running

# cisco(cli,ssh1)
# huawei(cli,ssh1)
def config_bkp(namet,configt):
    config = open('e:/Cisco/python/'+ namet+'_'+date1+ '.txt',mode='w+')
    config.write(configt)
    config.close()
    print(namet + ' config backup finished')

for device in range(len(devicelist)):
    name1 = devicelist[device]['device_name']
    ip1 = devicelist[device]['ip']
    username1 = devicelist[device]['username']
    password1 = devicelist[device]['password']
    plat = devicelist[device]['platfrom']
    try:
        if plat == 'IOS':
            running = cisco(ip1,username1,password1)
        elif plat == 'HW':
            running = huawei(ip1,username1,password1)
    except socket.error:
        unreachable_list.append(ip1)
    except paramiko.ssh_exception.AuthenticationException:
        auth_fail_list.append(name1)
    else:
        config_bkp(name1, running)
for i in unreachable_list:
    result = open('e:/Cisco/python/unreachable_list.txt',mode='w+')
    result.write(i  + ' - is unreachable')
    result.close()
    print(i + ' - is unreachable')
for i in auth_fail_list:
    result = open('e:/Cisco/python/auth_fail_list.txt',mode='a')
    result.write(i + ' - 由于某种原因身份认证失败引异常')
    result.close()
    print(i + ' - 由于某种原因身份认证失败引异常')
else:
    print('*'*80)
    print('Mission accomplished')
    print('*' * 80)


# paramiko常见异常参考
#http://docs.paramiko.org/en/stable/api/ssh_exception.html

