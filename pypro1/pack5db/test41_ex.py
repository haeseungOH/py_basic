# 사번과 이름을 입력하여 로그인에 성공하면 buser,jikwon : join
# 사번, 직원명, 부서명, 부서전화, 연봉, 성별 출력
# ex) 홍길동, 영업부, 123-1234, 12345,남

import MySQLdb
import pickle
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj)
   
def find():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jikwon_no = input('사번 입력:')
        jikwon_name = input('이름 입력:')
        jikwon_name1 = "'" + jikwon_name + "'"
    
        sql = """
            select jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen
            from jikwon j
            INNER JOIN buser b ON j.buser_num=b.buser_no
            where jikwon_no = {0} and jikwon_name = {1}
        """.format(jikwon_no,jikwon_name1)
        
        cursor.execute(sql)
        
        datas = cursor.fetchall()
        
        if len(datas) == 0:
            print('해당하지 않습니다.')
            return
        
        for jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen in datas:
            print(jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen)
            
    except Exception as e:
        print('error:',e)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    find()