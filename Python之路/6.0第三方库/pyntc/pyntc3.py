from pyntc import ntc_device as NTC

SW1 = NTC(host='203.0.113.1', username='qytang', password='qytang', device_type='cisco_ios_ssh')
SW1.open()

run = SW1.running_config
print(run)
SW1.close()

##读取设备配置