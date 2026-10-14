addr = "홍길"\
"동"
addr = """
    산골짜기
    홍길동
    여러 줄
"""

print(addr)

print("1. 쉬운 게임")
print("2. 어려운 게임")
print("3. 종료")
# num = int(input(">>>> "))
num = 1

if num == 1:
    print("쉬운 게임을 실행합니다.")
elif num == 2:
    print("어려운 게임을 실행합니다.")
else:
    print("종료합니다.")
print("---"*10)

num = int(input("수 입력: "))
if num%2 == 0:
    print("입력 값 짝수: ", num)
else:
    print("입력 값 홀수: ", num)

