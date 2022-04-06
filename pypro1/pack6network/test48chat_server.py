# 멀티 채팅 서버 : socket , thread 이용

import socket
import threading

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.93', 5555))     # host ip, port num 부여
ss.listen(5)                        # 동시에 5명접속 가능
print('채팅 서버 서비스 시작 ...')

users = []  # 채팅 접속 컴의 socket 의 갯수만큼 담는다. client가 담겨있다.

def chatUser(conn):
    name = conn.recv(1024)                  # 채팅 접속자를 전송
    data = '^i^ ' + name.decode('UTF_8') + '님 입장 ^^'
    print(data)                     
    
    try:
        for p in users:
            p.send(data.encode('UTF_8'))    # 모든 접속자에게 접속 채팅명을 전송.
        
        while True:
            msg = conn.recv(1024)           # 채팅 message 를 모든 접속자에게 전송
            data = name.decode('UTF_8') + '님 메세지:' + msg.decode('UTF_8')
            print(data)
            for p in users:
                p.send(data.encode('UTF_8'))
    except:                                 # client 가 접속을 해제하면 except를 만나게 된다.
        users.remove(conn)                  # 채팅을 종료한 client socket을 제거한다.
        data = '~~ ' + name.decode('UTF_8') + '님 퇴장 ~~'
        print(data)                         # 사용하지 않아도 된다.
        
        if users:
            for p in users:
                p.send(data.encode('UTF_8'))# 남아있는 client 에게 알려준다.
        else:
            print('exit')
                
while True:
    conn, addr = ss.accept()        # conn 은 socket
    users.append(conn)
    th = threading.Thread(target = chatUser, args = (conn,))
    th.start()                      # client가 접속 할 때마다 thread 가 만들어진다.
    
    