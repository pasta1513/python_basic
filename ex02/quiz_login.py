import sys

save_id = "aaa"
save_pw = "111"
input_id = input('id를 입력하시오. > ')

if input_id != save_id:
    print('존재하지 않는 회원입니다.')
    sys.exit() # 이미 id가 맞지 않으므로 pw 입력을 받지 않고 프로그램 강제 종료
else:
    pass

input_pw = input('pw를 입력하시오. > ')

if input_pw == save_pw:
    print('인증이 통과되었습니다.')
else:
    print('비밀번호가 틀렸습니다.')