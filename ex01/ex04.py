n1, n2 = 9, 2
print('-----===== 산술 연산자 =====-----')
print(n1 / n2)
print(n1 // n2)
print(n1 % n2)
print(n1 * n2)
print(n1 ** n2)
print('-----===== 관계 연산자 =====-----')
print(n1 > n2)
print(n1 <= n2)
print(n1 == n2)
print(n1 != n2)

print('-----===== 대입 연산자 =====-----')
su1 = su2 = 5
su1 += 1
print("su1 + 1 = " , su1)
su1 -= 1
print("su1 - 1 = ", su1)
su1 *= su2
print("su1 * su2 = ", su1)
su1 //= su2
print("su1 // su2 = ", su1)
su1 %= su2
print("su1 % su2 = ", su1)

su1 = 5
su2 = 3
su1 **= su2
su1 -= 2
print("su1 / 4 = ",su1 / 4)
print("su1 // 4 = ",su1 // 4)
print("su1 % 4 = ",su1 % 4)

print('-----===== 논리 연산자 =====-----')
print(True and True)
print(True and False)
print((10%2 == 0) and (10 < 5))
print(True or True)
print(True or False)
print((10%2 == 0) or (10 < 5))

user_id = "aaa"
user_pw = "bbb"
input_id = "aaa"
input_pw = "bbb"
print(input_id == user_id and input_pw == user_pw)

input_pw = "ccc"
print(input_id == user_id and input_pw == user_pw)
