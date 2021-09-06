import paramiko
import os

def exp(host,port,user,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port,user,password,timeout=5)
        ssh.close()
        return True
    except:
        return False


 if __name__ == "__main__":
    host = args[1]
    port = int(args[2])
    user = args[3]
    password = args[4]
    if exp(host,port):
        print("登录成功！")
    else:
        print("登录失败！")
        

    


