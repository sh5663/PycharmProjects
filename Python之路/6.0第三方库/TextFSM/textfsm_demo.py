from textfsm import TextFSM

output = '''
SW1#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi0/1, Gi0/2, Gi0/3, Gi1/0
                                                Gi1/1, Gi1/2, Gi1/3
10   VLAN0010                         active    
11   VLAN0011                         active    
12   VLAN0012                         active    
13   VLAN0013                         active    
14   VLAN0014                         active    
15   VLAN0015                         active    
16   VLAN0016                         active    
17   VLAN0017                         active    
18   VLAN0018                         active    
19   VLAN0019                         active    
20   VLAN0020                         active   
'''

f= open(r'D:\PycharmProjects\Python之路\6.0第三方库\TextFSM\show_vlan.template','r')
template = TextFSM(f)

print(template.ParseText(output))