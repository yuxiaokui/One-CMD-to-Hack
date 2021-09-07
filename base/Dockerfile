FROM kalilinux/kali-rolling

MAINTAINER  xi4okui@gmail.com

RUN apt update \ 
        && apt install -y  python3 python3-pip nmap git gobuster wfuzz \ 
        && pip install requests paramiko pycrypto \
        && apt clean \
        && rm -rf /var/lib/apt/lists/* 