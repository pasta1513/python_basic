import os

print(os.path.exists('test111.txt'))
file_name = 'ex05/test.txt'

if os.path.exists(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    print(file.read())
    file.close()

# .env 파일 내의 정보를 불러옴
# user에 대한 정보나 api key의 경우에는 공유 금지!!
print(os.getenv("USERNAME"))
print(os.getenv("PASSWORD"))

u_name = os.getenv("USERNAME")