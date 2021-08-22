import paramiko
import time

ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道

ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
ssh1.connect(hostname='203.0.113.3',port=22,username='qytang',password='qytang',timeout=5,allow_agent=False,
                 look_for_keys=False)
    # time.sleep(15)  #测试使用

sftp1=ssh1.open_sftp() #建立一个sftp连接
local_path=r'e:/Cisco/python/' #指定本地路径
remote_path='/' #指定远程路径
# sftp1.get(remote_path + 'vrpcfg.zip', local_path + 'vrpcfg.zip') #交换机为服务端拉取到本地
sftp1.put(local_path + 'SW3.txt',remote_path + 'test.txt') #本地为服务端推送到交换机
time.sleep(5)
ssh1.close()
