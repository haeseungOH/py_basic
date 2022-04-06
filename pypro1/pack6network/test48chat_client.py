# 멀티 채팅 클라이언트 : socket, thread

import socket
import threading
import sys

def handle(socket):         
    while True:
        data = socket.recv(1024)
        if not data:continue        # data 가 없으면 출력하지 않는다.
        print(data.decode('UTF_8'))
        
sys.stdout.flush()                  # 파이썬의 표준 출력은 버퍼링이 된다. 표준 출력장치를 청소해주는 역활 

name = input('채팅명 입력 :')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.93', 5555))  # 접속할 HOST ip 주소 입력
cs.send(name.encode('UTF_8'))

th = threading.Thread(target = handle, args = (cs,))
th.start()

while True:
    msg = input()                   # 채팅 message를 입력
    sys.stdout.flush()
    if not msg:continue             # message 를 입력하지 않으면 send X
    cs.send(msg.encode('UTF_8'))
    
cs.close()