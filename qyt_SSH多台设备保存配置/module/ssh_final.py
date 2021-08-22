from ssh_devicelist import devicelist
from ssh_client import *
from ssh_config_bkp import *
import socket
unreachable_list = []
auth_fail_list = []

for device in range(len(devicelist)):
    name1 = devicelist[device]['device_name']
    ip1 = devicelist[device]['ip']
    username1 = devicelist[device]['username']
    password1 = devicelist[device]['password']
    plat = devicelist[device]['platform']
    try:
        if plat == 'IOS':
            running = cisco(ip1, username1, password1)
        elif plat == 'HW':
            running = huawei(ip1, username1, password1)
    except socket.error:
        unreachable_list.append(ip1)
    except paramiko.ssh_exception.AuthenticationException:
        auth_fail_list.append(name1)
    else:
        config_bkp(name1, running)
for i in unreachable_list:
    result = open('e:/Cisco/python/unreachable_list.txt', mode='w+')
    result.write(i + ' - is unreachable')
    result.close()
    print(i + ' - is unreachable')
for i in auth_fail_list:
    result = open('e:/Cisco/python/auth_fail_list.txt', mode='a')
    result.write(i + ' - 由于某种原因身份认证失败引异常')
    result.close()
    print(i + ' - 由于某种原因身份认证失败引异常')
else:
    print('*' * 80)
    print('Mission accomplished')
    print('*' * 80)
