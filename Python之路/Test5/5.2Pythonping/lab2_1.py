from pythonping import ping
import os
if os.path.exists(r'D:\PycharmProjects\Python之路\Test5\5.2Pythonping\reachable_ip.txt'):
    os.remove(r'D:\PycharmProjects\Python之路\Test5\5.2Pythonping\reachable_ip.txt')
third_octet = range(113,114)
last_octet = range(1,255)
for ip3 in third_octet:
    for ipv4 in last_octet:
        ip = '203.0.'+ str(ip3) + '.'+str(ipv4)
        ping_result = ping(ip)
        # print(ping_result)
        f = open(r'D:\PycharmProjects\Python之路\Test5\5.2Pythonping\reachable_ip.txt','a')
        if 'Reply' in str(ping_result):
            print(ip + ' is reachable.')
            f.write(ip + '\n')
        else:
            print(ip +' is not reachable.' )
        f.close()
