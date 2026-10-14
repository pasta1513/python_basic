name = "yuna"
print(name)
num = 100
print(num)
print(f"변경전 num: {num}")

num = 200
print(f"변경 후 num: {num}")

num += 5
print(f"변경 후 num: {num}")

n1, n2 = 5, 10
sum_ = n1 + n2
print(f"{n1} + {n2} = {sum_}")

print(type(name))
print(type(n1))
print(type(12.345))
print(type("10"))

n1, n2 = 10, 20
print(n1 + n2)
n1, n2 = "10", "20"
print(n1 + n2)

num = 10
str1 = "20"
str2 = "안녕"
print(str(num))
print(type(str(num)))
print(int(str1))
# print(int(str2)) # 형변환 불가능
