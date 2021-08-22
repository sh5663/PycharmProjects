import paramiko
import time


ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
ssh1.connect(hostname='203.0.113.1',port=22,username='qytang',password='qytang',timeout=5,allow_agent=False,
                 look_for_keys=False)
    # time.sleep(15)  #测试使用

cli_connect = ssh1.invoke_shell()
cli_connect.send('enable\n')
time.sleep(1)
cli_connect.send('qytang\n')
time.sleep(1)
cli_connect.send('configure terminal\n')
time.sleep(1)
cli_connect.send('file prompt quiet \n') #为文件名确认使用
time.sleep(1)
cli_connect.send('end\n')
time.sleep(1)
cli_connect.send('copy running-config ftp://203.0.113.6 \n')
time.sleep(1)
print(cli_connect.recv(99999).decode())
time.sleep(3)
ssh1.close()
