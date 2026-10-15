num = 10
if num > 5:
    print('입력 값은 5보다 크다.')
else: # n <= 5
    print('입력 값은 5보다 작거나 같다.')

print('--'*20)

num = 12
if num%3 == 0:
    if num%2 == 0:
        print('6의 배수이다.')
else:
    print('3의 배수가 아니다.')