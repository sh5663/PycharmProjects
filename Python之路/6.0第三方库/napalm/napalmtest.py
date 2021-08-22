from napalm import get_network_driver
import json
driver = get_network_driver('ios')
SW1 = driver('203.0.113.1','qytang','qytang')
SW1.open()
output = SW1.get_arp_table()
print(json.dumps(output,indent=2))