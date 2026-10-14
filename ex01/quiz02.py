num1 = input('올해의 년도를 4자리로 입력하세요: ')
num2 = input('당신이 태어난 년도를 4자리로 입력하세요: ')
age = int(num1) - int(num2) + 1
print(f'당신의 나이는 {age}살입니다.')

weight1 = input('첫 번째 물건의 무게를 입력하시오: ')
weight2 = input('두 번째 물건의 무게를 입력하시오: ')
weight = 600 - (float(weight1) + float(weight2))
print(f'현재 엘리베이터의 허용 무게는 {weight} kg입니다.')

height = float(input('당신의 키를 입력하시오: '))
standard_weight = (height - 100) * 0.9
weight = float(input('현재 몸무게를 입력하시오: '))
obesity = (weight/standard_weight) * 100
print(f'표준 체중은 {standard_weight} 이고, \n비만도는 {obesity:.2f} 입니다.')

name = input('이름을 입력하시오: ')
Korean_score = int(input('국어 점수를 입력하시오: '))
English_score = int(input('영어 점수를 입력하시오: '))
Mathematics_score = int(input('수학 점수를 입력하시오: '))
total_score = Korean_score + English_score + Mathematics_score
average = (total_score) / 3
print('==================== 학생 정보 ====================')
print(f'{"이름":<6} {"국어":<4} {"영어":<4} {"수학":<4} {"합계":<4} {"평균":<0}')
print('-' * 50)
print(f'{name:<6} {Korean_score:<6} {English_score:<6} {Mathematics_score:<6} {total_score:<6} {average:>0.2f}')
