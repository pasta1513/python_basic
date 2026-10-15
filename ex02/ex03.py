# i=1, i<11, i+=1
for i in range(1, 11, 1):
    print(i)

num = 5
for i in range(1, num+1):
    if i%2 == 0:
        print(f'{i}: 짝')
    else:
        print(f'{i}: 홀')

print('-'*30)

for i in range(1, 11):
    print(i, end=' ')

print('-'*30)

for i in range(1, 31):
    if i%5 != 0:
        print(i, end=' ')
    else:
        print(i)

print('-'*30)

st = 'abcd1234'
for i in st:
    print(i)

li = [10, 20, 30, 40]
for i in li:
    print(i)