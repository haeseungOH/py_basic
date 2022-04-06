# 원격 데이터베이스 연동
import MySQLdb              # 드라이브 파일을 모듈로 처리 

#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
#print(conn)
#conn.close

config = {                  # dict type으로 data 작성
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',       # utf-8 X
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)                # dict type 이기 때문에 **개 사용
    cursor = conn.cursor()
    
    """
    print('insert ---')                             # insert 는 1개밖에 못한다.
    #isql = "insert into sangdata(code,sang,su,dan) values(10,'신상',5,5000)"
    #isql = "insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)"
    isql = "insert into sangdata values(%s,%s,%s,%s)"
    sql_data = (10,'신상',5,5000)
    #sql_data = 10,'신상',5,5000
    cursor.execute(isql, sql_data)
    conn.commit()
    """
    
    """
    print('update ---')
    usql = "update sangdata set sang=%s,su=%s where code=%s"
    sql_data = ('얼죽아',30,10)
    cou = cursor.execute(usql, sql_data)
    print('cou : ', cou)
    conn.commit()
    """
    
    """
    print('delete ---')
    input_code = '10'
    #dsql = "delete from sangdata where code =" + input_code              #secure coding 가이드 라인에 위배
    
    #dsql = "delete from sangdata where code=%s"
    #cou = cursor.execute(dsql, (input_code,))                            #tuple은 (xxx,(xxx,)) <- 작성법
    
    dsql = "delete from sangdata where code='{0}'".format(input_code)
    cou = cursor.execute(dsql)
    conn.commit()
    if cou > 0:
        print('삭제 성공')
    else:
        print('삭제 실패')
    """
    
    print('select ---')
    sql = 'select code,sang,su,dan from sangdata'   # select * from sangdata 비추천
    cursor.execute(sql)                             # 두개이상 레코드를 읽는 방법은 없다.
    
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
    """    
    print()
    for data in cursor:
        print(data[0],data[1],data[2],data[3])
    
    print()                                         # 가독성을 위해서 칼럼명으로 cursor 변수 설정 추천
    for (code,sang,su,dan) in cursor:
        print(code,sang,su,dan)
    
    print()
    for (a,kbs,mbc,dan) in cursor:
        print(a,kbs,mbc,dan)
        
    """       
except Exception as e:          
    print('err:',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
