'''class CoinIn:
    def __init__(self,coin):
        self.coin=coin
    def culc(self,cupCount):
        total=cupCount*200
        if self.coin<total:
            return '금액이 부족합니다'
        else:
            self.coin-=total
            return '커피 {}잔과 잔돈 {}원'.format(cupCount,self.coin)

class Machine:
    def __init__(self):
        self.coin=int(input("동전을 입력하세요 : "))
        self.cupCount=int(input("몇 잔을 원하세요 : " ))
        
    def showData(self):
        insertCoin=CoinIn(self.coin)
        print(insertCoin.culc(self.cupCount))

Machine().showData()
'''
