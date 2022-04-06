# Module : 소스 코드의 재사용을 가능하게 하며, 소스 코드를 하나의 이름 공간으로 구분하고 관리한다.
# 파이썬은 모듈 단위로 파일로 저장된다.
# 모듈의 멤버 : 변수, 실행문, 함수, 클래스
# main module 확인 : __name__ == '__main__'

# 내장된 모듈
print('뭔가를 하다가...')

import sys
print(sys.path)     #경로를 알려준다.
#sys.exit()         프로그램 강제 종료

import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)     # 0 ~ 6
calendar.prmonth(2022, 3)

print(dir(calendar))

import time
print(time.localtime())
#print('start...')
#time.sleep(3)                   # 일정 시간동안 프로그램을 재울수 있다.
#print('finish')

import os
print(os.getcwd())              # 현재 작업 경로를 보여준다.

print()
import random
print(random.random())
print(random.randint(1, 10))

from random import randint
print(randint(1, 10))

from random import  *           # 권장 하지 않는다
print(random())
print('프로그램 종료')
