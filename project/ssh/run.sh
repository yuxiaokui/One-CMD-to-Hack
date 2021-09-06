docker build -t ssh_login .
docker run --rm ssh_login ssh 8.8.8.8 22 root root
