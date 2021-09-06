FROM python:slim
MAINTAINER xi4okui@gmail.com
WORKDIR hacker
ADD * /hacker
RUN pip install -r requirement.txt
ENTRYPOINT python3 ssh_login.py $@