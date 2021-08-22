import ssl
from pysphere import VIServer

ssl._create_default_https_context = ssl._create_unverified_context

host_ip = xx.xx.xx.xx // VMwareIP地址
username = "xxx" // VMware用户名
passwd = "xxx" // VMware密码
vmware_name = "xxx" // 虚拟机名字
server_obj = VIServer()
server_obj.connect(host=host_ip, user=username, password=passwd)
vm1 = server_obj.get_vm_by_name(vmware_name)
status = vm1.is_powered_off()
if status == True:
    poweron = vm1.powered_on()
elif status == False:
    poweroff = vm1.powered_off()
