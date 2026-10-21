class Test01:
    # n1 = None
    # n2 = None
    # sum = None

    def sum_func(self):
        self.sum = self.n1 + self.n2

    def input_num(self):
        self.n1 = int(input('첫 번째 수 입력: '))
        self.n2 = int(input('두 번째 수 입력: '))
    
    def  print_sum(self):
        print(f'{self.n1} + {self.n2} = {self.sum}')

# t = Test01()
# t.input_num()
# t.sum_func()
# t.print_sum()

class Test02:
    def __init__(self, addr : str = None):
        print('생성자 실행?')
        self.name = '홍길동'
        self.addr = addr

    def print_(self):
        print(self.name)
        print(self.addr)

addr = '산골짜기'
t02 = Test02(addr)
# print(t02.name)
# print(t02.addr)
t02.print_()