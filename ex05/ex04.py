try:
    age = int(input('당신의 나이 입력: '))

    if age < 1:
        # raise 강제 예외(Exception) 발생
        raise Exception('문제 발생!')
except ValueError:
    print('숫자를 입력하세요.')
except Exception as e:
    print(e, '1살 아래의 나이는 없습니다.')
else:
    print('당신의 나이는 ', age, '입니다.', sep='')
finally:
    print('프로그램을 종료합니다.')