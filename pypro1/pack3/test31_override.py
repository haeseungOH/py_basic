# 메소드 오버라이드 : 다형성

class Parent:
    def printData(self):
        pass 
    
class Child1(Parent):           # override
    def printData(self):        
        print('Child에서 override')
 
class Child2(Parent):
    def printData(self):        
        print('Child2에서 재정의')
        print('부모 메소드와 이름은 같으나 기능이 다름')
        
    def abc(self):
        print('Child2 고유 메소드')
        
c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()
c2.abc()

print('\n다형성 ---')
#par = Parent()             # python 에서는 부모 객체변수를 만들지 않아도 된다.
par = c1                    # Child1 에 있는 printData 수행
par.printData()             
print('---' * 10)
par = c2                    # Child2 에 있는 printData 수행
par.printData()
par.abc()

print('---' * 10)
plist = [c1, c2]            # c1,c2 의 printData를 순서대로 수행
for a in plist:
    a.printData()