from pyntc import ntc_device as NTC

SW1 = NTC(host='203.0.113.1', username='qytang', password='qytang', device_type='cisco_ios_ssh')
SW1.open()

SW1.config('hostname SW1')
SW1.config_list(['router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0'])
SW1.close()

#对设备进行配置,脚本会报错但是配置正常下发