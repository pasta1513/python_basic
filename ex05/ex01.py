# 'w' write 모드 -> 파일에 기존 내용이 있다면 기존 내용을 모두 지우고 새 내용으로 덮어씀
# 'a' append 모드 -> 기존 내용 뒤에 새 내용을 추가하고 싶다면
# 'r' read 모드 -> 파일의 내용을 읽을 때 사용, 파일이 없다면 FileNotFoundError
# 'x' exclusive creation 모드 -> 파일을 새로 생성, 이미 같은 이름의 파일이 있다면 FileExistsError
file = open('./ex05/test.txt', 'w', encoding='utf-8')
str1 = input('파일에 저장할 내용 입력: ')
file.write(str1 + '\n')
file.close()

str2 = input('파일에 저장할 내용 입력: ')
# with를 사용하면 close 역할을 함께 수행해줌
with open('./ex05/test.txt', 'a', encoding='utf-8') as file:
    file.write(str2)

with open('ex05/test.txt', 'r', encoding='utf-8') as file:
    print(file.read())

with open('ex05/test2.txt', 'x', encoding='utf-8') as file:
    file.write('새 파일입니다')

# \의 경우 특수한 상황에 많이 사용되기 때문에 경로 표현 시 2개씩 사용 or / 사용
str3 = 'C:\\yuna-workspace\\python-workspace'
print('str3: ', str3)