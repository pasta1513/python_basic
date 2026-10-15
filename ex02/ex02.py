num = int(input('입력하시오: '))

if num > 100:
    print('100보다 크다.')
elif num > 50:
    print('50보다 크고 100보다 작거나 같다.')
elif num > 0:
    print('0보다 크고 50보다 작거나 같다.')
else:
    print('그 외의 값')
print('다음 문장들 실행!')