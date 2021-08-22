import paramiko
import time

def cisco(ipt,usernamet,passwordt):
    ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
    ssh1.connect(hostname=ipt,port=22,username=usernamet,password=passwordt,timeout=5,allow_agent=False,
                 look_for_keys=False)
    # time.sleep(15)  #测试使用

    cli = ssh1.invoke_shell()
    cli.send('terminal len 0\n')
    time.sleep(1)
    cli.send('show run\n')
    time.sleep(5)
    run_config  = cli.recv(99999).decode()
    # print(running)
    ssh1.close()
    return run_config

def huawei(ipt,usernamet,passwordt):
    ssh1 = paramiko.SSHClient()  # 实例化SSH客户端会话通道
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 默认秘钥处理策略
    ssh1.connect(hostname=ipt, port=22, username=usernamet, password=passwordt, timeout=5, allow_agent=False,
                 look_for_keys=False)
    # time.sleep(15)  #测试使用

    cli = ssh1.invoke_shell()
    cli.send('screen-length 0 temporary\n')
    time.sleep(1)
    # cli.send('sys\n')
    # time.sleep(1)
    cli.send('disp cu\n')
    time.sleep(5)
    run_config  = cli.recv(99999).decode()
    # print(running)
    ssh1.close()
    return run_config

# cisco(cli,ssh1)
# huawei(cli,ssh1)


