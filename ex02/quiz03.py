# num = int(input('몇 Gbyte인가요? > '))
# unit = int(input('변환할 단위를 선택하세요. \n1. byte 2. Kbyte 3. Mbyte > '))

# if unit == 3:
#     num *= 1024
#     print(f'{num} Mbyte입니다.')
# if unit == 2:
#     num *= (1024 ** 2)
#     print(f'{num} Kbyte입니다.')
# if unit == 1:
#     num *= (1024 ** 3)
#     print(f'{num} byte입니다.')

# num = int(input('정수를 입력하시오. > '))

# if num!=0 and num%3==0:
#     if num%4 == 0:
#         print('3의 배수이면서 4의 배수')
#     else:
#         print('3의 배수')
# elif num!=0 and num%4==0:
#     print('4의 배수')
# else:
#     print('둘 다 아님')

# 비행기 요금은 30분까지 기본 30000원이고, 이후 10분 단위로 5000원씩 추가된다. 탑승 시간(분)을 입력받아 요금을 계산하시오. (예: 31~40분은 35000원)