import paramiko
import sys

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
    host = sys.argv[1]
    port = int(sys.argv[2])
    user = sys.argv[3]
    password = sys.argv[4]
    if exp(host,port,user,password):
        print("登录成功！")
    else:
        print("登录失败！")
        

    


