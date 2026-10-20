try:
    n1 = int(input('수 입력: '))
    n2 = 2

    div = n1 / n2
    print('나눈 결과 ', div)
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
except ValueError as v_error:
    print('숫자만 입력해주세요.\n', v_error, sep='')
    # 쉼표로 구분된 값 사이에는 기본적으로 공백 하나(sep=' ')가 포함된 채 출력됨
    # 공백을 없애고 싶다면 sep='' 옵션을 사용!
except:
    print('모든 예외를 전부 처리')

print('다음 실행')