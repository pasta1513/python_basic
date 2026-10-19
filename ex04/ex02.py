print('프로그램 실행')

def sum_func():
    sum = 0
    num = int(input('수 입력: '))

    for i in range(num+1):
        sum += i
    print(f'1 ~ {num}까지의 합: {sum}')

# sum_func()
# print('프로그램 종료')

def sum_func1(num):
    sum = 0
    # num = int(input('수 입력: '))

    for i in range(num+1):
        sum += i
    print(f'1 ~ {num}까지의 합: {sum}')

# num = int(input('수 입력: '))
# sum_func1(num)

def sum_func2(num : int):
    '''
    이 기능은 사용자가 1부터 입력한 수까지의 합을 구합니다.
    '''
    sum = 0

    for i in range(num+1):
        sum += i

    return sum

num = int(input('수 입력: '))
sum = sum_func2(num)
print(f'1 ~ {num}까지의 합: {sum}')