# 추상 클래스 연습문제 4번문제
from abc import * 

class Employee(metaclass = ABCMeta):    #추상 메소드를 가지고 있다.
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    
    @abstractclassmethod                #추상 메소드
    def pay(self):
        pass
    
    @abstractclassmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print('이름 : ' + self.irum + ', 나이 : ' + str(self.nai), end=' ')
        

class Temporary(Employee):
    def __init__(self, irum, nai, ilsu, ildang ):
        Employee.__init__(self, irum, nai)      #irum, nai 를 부모에게 넘긴다.
        self.ilsu = ilsu
        self.ildang = ildang
    
    def pay(self):
        return self.ilsu * self.ildang
    
    def data_print(self):
        self.irumnai_print()
        print(', 월급 : ' + str(self.pay()))

    
class Regular(Employee):
    def __init__(self, irum, nai, salary):
        super().__init__(irum, nai)             #부모의 생성자를 부르기 위해 형식적으로 super().__init__(irum,nai)을 사용한다.
        self.salary = salary
    
    def pay(self):
        return self.salary  
    
    def data_print(self):
        self.irumnai_print()
        print(', 급여 : ' + str(self.pay()))

class Salesman(Regular):
    def __init__(self, irum, nai, salary, sales, commission):
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
     
    def pay(self):
        return super().pay() + (self.sales * self.commission)  
    
    def data_print(self):
        self.irumnai_print()
        print(', 수령액 : ' + str(self.pay()))   
    
        
t = Temporary('홍길동', 25, 20, 15000)
t.data_print()

r = Regular('한국인', 27, 3500000)
r.data_print()

s = Salesman('손오공', 29, 1200000,5000000, 0.25)
s.data_print()


    