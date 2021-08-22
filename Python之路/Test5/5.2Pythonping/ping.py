
import subprocess
target = 'www.baidu.com'
ping_reuslt = subprocess.call(['ping',target])
if ping_reuslt ==0:
    print(target + ' is reachable')
else:
    print(target + ' is not reachable')
