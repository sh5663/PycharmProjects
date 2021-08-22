import json

from pyntc import ntc_device as NTC

SW1 = NTC(host='203.0.113.1',username='qytang',password='qytang',device_type='cisco_ios_ssh')
SW1.open()

print(json.dumps(SW1.facts(),indent=4))

SW1.close()

#facts问题无法进行下去

