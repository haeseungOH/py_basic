# 단순 Echo Server 

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)   # socket(소켓종류, 소켓유형) = socket객체 생성
serverSock.bind(('127.0.0.1', 8888))        # socket을 컴퓨터에 bind
serverSock.listen(1)                        # 1 ~ 5 까지의 값을 줄 수 있다.
print('server start...')

conn, addr = serverSock.accept()            # 연결 대기 설정 
print('client addr : ', addr)
print('from client message : ', conn.recv(1024).decode())   # client로 부터 message를 받아서 출력
conn.close()
serverSock.close()
