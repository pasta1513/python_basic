print('name: ', __name__)

def test_func():
    temp = 0
    result = int(input('수 입력: '))
    while True:
        temp = result % 10
        result = result // 10
        print(temp, end=', ')
        if not result:
            break
    print('프로그램 종료!')

print('test 목적 ex01 실행 중')