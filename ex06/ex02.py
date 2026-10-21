class Test01:
    def sum_func(self, n1, n2):
        sum = n1 + n2

        return sum

    def input_num(self):
        n1 = int(input('첫 번째 수 입력: '))
        n2 = int(input('두 번째 수 입력: '))

        return n1, n2
    
    def  print_sum(self, n1 ,n2, s):
        print(f'{n1} + {n2} = {s}')

t = Test01()
n1, n2 = t.input_num()
s = t.sum_func(n1 ,n2)
t.print_sum(n1 ,n2, s)