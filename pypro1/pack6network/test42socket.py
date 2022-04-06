# 파이썬 네트워크
# 네트워크를 위한 통신 채널을 지원 : socket 모듈

import socket       # socket 사용준비

print(socket.getservbyname('http', 'tcp'))      # http port num :80
print(socket.getservbyname('telnet', 'tcp'))    # telmet port num :23
print(socket.getservbyname('ftp', 'tcp'))       # ftp port num :21
print(socket.getservbyname('smtp', 'tcp'))      # smtp port num :25
print(socket.getservbyname('pop3', 'tcp'))      # pop3 port num :110

print(socket.getaddrinfo('www.naver.com', 80, proto = socket.SOL_TCP))
# 223.130.195.95, 223.130.195.200    naver ip address




