# Web server : 클라이언트와 통신이 가능
# CGI (Common Gateway Interface)
# : 웹서버와 외부프로그램 사이에서 정보를 주고 받는방법이나 규약. 대화형 웹 페이지 작성 가능.
# : DB 자료 처리, form tag를 사용한 자료 전송 가능
# 쿠키,세션,request,response 용어 정리하기..
from http.server import HTTPServer, CGIHTTPRequestHandler   #python sql 사용을 위해 CGIHTTPRequestHandler을 이용 

PORT = 8888

class Handler(CGIHTTPRequestHandler):           # servlet 같이 사용할 수있게 해준다.
    cgi_directories = ['/cgi-bin']
    
serv = HTTPServer(('127.0.0.1', PORT), Handler)

print('웹서비스 시작 ...')

serv.serve_forever()    # 무한 루프에 빠진다.

