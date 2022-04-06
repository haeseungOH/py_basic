# 묶음 자료형
# 자료형 중에서 int, float, bool, complex : 객체 하나를 참조
# 자료형 중에서 str, list, tuple, set, dict : 객체값 여러 개를 요소로 참조


# str : 문자열 자료형. 순서O : 인덱싱, 슬라이싱 기능, 수정X
s = 'sequence'
print('길이:', len(s))
print('특정문자 포함 위치 확인 : ', s.count('e'),s.count('m'), s.find('e'))
# 다량의 문자열 관련 함수
print(id(s))
s='bequence'    #새로운 객체를 치환
print(id(s))

#인덱싱, 슬라이싱 가능 
s = 'sequence'
print(s,s[0],s[3],s[7], s[-1], s[-3])
print(s[0:3])   # 0 이상 3미만    [시작:끝:간격]
print(s[-4:-1]) # enc
print(s[:3])    # seq
print(s[3:])    # uence
print(s[2:7:1]) # quenc
print(s[2:7:2]) # qec
print(s[::2])   # sqec
print(s[2:5]+'만세')

ss='mbc kbs'
result=ss.split(sep =' ')
print(result)
print(','.join(result))

print('\n\nlist type--- : 순서O, 수정O, 요소값 중복O. 요소들은 []로 감쌈')
a=[1,2,3,'문자열',4.5,True, 1,2,3]
print(a, type(a))
b=[a,100,200]   #중복 리스트
print(b)

print()
family=['엄마','아빠']
print(id(family))
family[0]='어머니'
print(id(family))
family.append('나')  #많이 쓰인다.
family.insert(1, '여동생')
family.extend(['삼촌','이모'])
family += ['고모']
print(family)

family.remove('나')  # 값에 의한 삭제
# family.remove('나')
del family[0]       # 순서에 의한 삭제
del family[0]
print(family)
del family          # 변수를 삭제할 때
# print(family)

print('\n\nTuple type--- : 리스트와 유사. 수정X. 요소들은 ()로 감쌈')
t=('a',10,'b')
t='a',10,'b'    #위와 동일
print(t, type(t))
print(t[0])
#t[0]='k'       #TypeError: 'tuple' object does not support item assignment
a=(1)           #<class 'int'>
b=(1,)          #<class 'tuple'>
print(type(a),type(b))

# 형변환
aa=[1,2,3]      
bb=tuple(aa)
print(type(bb))
aa=list(bb)
print(type(aa))

print('\n\nSet type--- : 순서X. 수정X. 중복 불가. 요소들을 {}로 감쌈')
a={1,2,3,1}
print(a,type(a))
#print(a[0])     #TypeError: 'set' object is not subscriptable
b={3,4}
print(a.union(b))
print(a.intersection(b))
print(a - b, a | b, a & b)

b.update({5,6})
b.update({7,8})
b.update({9,10})
print(b)
b.discard(6)
#b.discard(6)    # 해당 값이면 통과
b.remove(7)
#b.remove(7)     # 해당 값이면 에러
print(b)

aa=[1,2,2,3,5,5]
bb=set(aa)
print(bb)
aa=list(bb)
print(aa,type(aa))

print('\n\ndict type--- : 순서X. 수정O. 요소들을 {"키":"값"}로 감쌈')
mydic=dict(k1=1,k2='abc',k3=3.4)
print(mydic,type(mydic))

dic = {'파이썬':'뱀','자바':'커피','스프링':['용수철','웹처리']}
print(dic)
print(dic['파이썬'])
#print(dic[0])   #err

dic['오라클']='예언자'
print(dic)
del dic['오라클']
print(dic)
dic['파이썬']='만능 언어'
print(dic)

