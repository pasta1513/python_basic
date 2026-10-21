class Calc:
    def calc(self):
        print('계산기 실행')

# ca = Calc()
# ca.calc()

class Computer(Calc):
    def com(self):
        print('컴퓨터 실행')

c = Computer()
c.com()
c.calc()

class Ferrari:
    def __init__(self, year : int = 2026):
        self.year = year

    def speed(self):
        print(f'{self.year}년식 페라리의 속도: 300km/h')

class NewFerrari(Ferrari):
    def auto_system(self):
        print('자동 운전 모드 실행')

    def speed(self):
            print(f'{self.year}년식 페라리의 속도: 500km/h')

f = Ferrari()
f.speed()
f1 = NewFerrari(2027)
f1.speed()
f1.auto_system()