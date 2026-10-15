i = 1
while i < 11:
    print(i)
    i += 1

print('-'*30)

i = 1
while i < 11:
    if i%2 == 0:
            print(f'{i}: 짝')
    else:
        print(f'{i}: 홀')
    i += 1

print('-'*30)

i = 0
while i < 5:
    i += 1
    if i == 3:
        # continue # 이 밑은 건너뛰고 다음 단계부터 이어서
        break # 반복문 중단
        print(33333)
    print(f'{i} 출력')

print('-'*30)

sum = 0
for i in range(1, 11):
    sum += i
print('최종 1 ~ 10까지의 합: ', sum)

num1 = int(input('첫 번째 수를 입력하세요. > '))
num2 = int(input('두 번째 수를 입력하세요. > '))
start_num = min(num1, num2)
end_num = max(num1, num2)
sum = 0
for i in range(start_num, end_num+1):
    sum += i
print(f'{start_num} ~ {end_num} = {sum}')