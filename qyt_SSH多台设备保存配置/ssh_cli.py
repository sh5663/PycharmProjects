import paramiko
import time


ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
ssh1.connect(hostname='203.0.113.1',port=22,username='qytang',password='qytang',timeout=5,allow_agent=False,
                 look_for_keys=False)
    # time.sleep(15)  #测试使用

cli = ssh1.invoke_shell()
time.sleep(3)
cli.close()
