from qytang_devicelist import devicelist
from qytang_CONFIG import *
from qytang_netconf_connect import netconf_connect

for i in range(len(devicelist)):
    device_name = devicelist[i]['name']
    device_ip = devicelist[i]['ip']
    device_port = devicelist[i]['netconf_port']
    device_username = devicelist[i]['username']
    device_password = devicelist[i]['password']
    device_params = devicelist[i]['params']

    if device_params == 'csr':
        CONFIG=[CONFIG0,CONFIG6]
    elif device_params == 'huawei':
        CONFIG=[CONFIG4,CONFIG5]
    m = netconf_connect(device_ip, device_params,device_port,
    device_username, device_password,)
    for CONFIG_final in CONFIG:
        m.edit_config(target='running', config=CONFIG_final)

