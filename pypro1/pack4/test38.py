# 우편번호 data 파일 사용
# 키보드로 동이름을 입력해서 해당 동이름의 자료만 읽기

try:
    dong = input('동이름 입력 :')
    #dong = '신사'
    #print(dong)
    
    with open(r'zipcode.txt', 'r', encoding = 'euc-kr') as f:
        line = f.readline()
        #print(line)
        
        while line:
            #lines = line.split('\t')        
            lines= line.split(chr(9))       # tab(HT(9) = ascii code) 으로 자르기 ,enterkey ascii code=(10,13)
            
            #print(lines)
            if lines[3].startswith(dong):
                print('[' + lines[0] + ']' + lines[1] + ' '+ \
                      lines[2] + ' ' + lines[3] + ' ' + lines[4])   # 우편번호는 [ 로 감싸고 lines[0]번째
            
            line = f.readline()

except Exception as e:
    print('err : ', e)