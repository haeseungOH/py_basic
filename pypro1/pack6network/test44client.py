# 단순 client

import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('192.168.0.10', 7878))          # server ip 입력 (선생님주소)
clientSock.sendall(' '.encode('UTF_8'))             # server에 전달할 내용 입력
re_msg = clientSock.recv(1024).decode()
print('수신 자료 : ', re_msg)
clientSock.close()
