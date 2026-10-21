class SumFunc:
    def sum_func():
        pass

class Info:
    name = None
    addr = None
    age = None

# 다른 파일에서 해당 파일을 참고할 때
# import ex01 → 모듈 전체를 가져오지만, 최상위 코드도 실행
# from ex01 import Info → Info를 가져오지만, 마찬가지로 최상위 코드가 실행
# if __name__ == '__main__': → 해당 파일을 직접 실행할 때만 그 안의 코드를 실행
if __name__ == '__main__':
    i = Info()
    i.name = 'name'
    i.addr = 'address'
    i.age = 10

    print(i)
    print(i.name)
    print(i.addr)
    print(i.age)

class MyClass:
    addr = '산골짜기'
    def test(self):
        print('test 메소드')
        print(self)
        self.name = '홍길동'
        print('test addr: ', self.addr)

if __name__ == '__main__':
    my_class = MyClass()
    my_class.test()
    print(my_class)
    print(my_class.name)
    print(my_class.addr)