from ncclient import manager

def netconf_connect(host_ip,params, port=830, user='qytang', password='Dashu666!'):
    x = manager.connect(host=host_ip,
                       port=port,
                       username=user,
                       password=password,
                       hostkey_verify = False,
                       device_params={'name':params},
                       allow_agent = False,
                       look_for_keys = False)
    return x

if __name__ == '__main__':
    from device_list import devicelist
    from CONFIG_xml import *

    for i in range(len(devicelist)):
        device_name = devicelist[i]['name']
        device_ip = devicelist[i]['ip']
        device_port = devicelist[i]['netconf_port']
        device_username = devicelist[i]['username']
        device_password = devicelist[i]['password']
        device_params = devicelist[i]['params']

        if device_params == 'csr':
            CONFIG = [CONFIG0, CONFIG6]
        elif device_params == 'huawei':
            CONFIG = [CONFIG4, CONFIG5]
        m = netconf_connect(device_ip,device_params, device_port,
                            device_username, device_password )
        for CONFIG_final in CONFIG:
            m.edit_config(target='running', config=CONFIG_final)
