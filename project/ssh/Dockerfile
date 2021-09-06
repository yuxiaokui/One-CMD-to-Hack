FROM python:slim
MAINTAINER xi4okui@gmail.com

WORKDIR /opt
ADD * /opt
RUN pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/
ENTRYPOINT python3 ssh_login.py $@
