import telnetlib
hostIP = '203.0.113.1'
user = 'qytang'
password = 'qytang'
tn = telnetlib.Telnet(hostIP)
tn.read_until(b'Username:')
tn.write(user.encode('ascii') +b'\n')
tn.read_until(b'Password: ')
tn.write(password.encode('ascii') + b'\n')

tn.write(b'conf t\n')
tn.write(b'int loo 1\n')
tn.write(b'ip add 1.1.1.1 255.255.255.255\n')
tn.write(b'end\n')
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))
