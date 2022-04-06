# Echo Server : 서비스를 계속 유지
import socket
import sys

#HOST = '192.168.0.93'  
HOST = ''               # 자동으로 내 ip가 잡힌다.
PORT = 7878

serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serSock.bind((HOST, PORT)) 
    serSock.listen(5)                       # 동시 최대 접속 수 : 1 ~ 5
    print('서버 서비스 중 ...')
    
    while True:
        conn, addr = serSock.accept()       # client 가 connect 하는 순간   
        print('client info : ', addr[0], addr[1])
        print(conn.recv(1024).decode())     # message 수신
        
        # message 송신
        conn.send(('from server : ' + str(addr[0]) + ', 너도 잘 지내라 ~').endcode('UTF_8'))
            
except Exception as e:
    print('err : ', e)
    sys.exit()
finally:
    serSock.close()
    conn.close()
    