def test1():
    a = 100
    print('test1: a = ', a)
    return a

def test2(num):
    print('test2: a = ', num)

num = test1()
test2(num)

def test3():
    print('test2: b = ', b)

def test4():
    global b
    b = 100
    print('test2: b = ', b)

b = 12345
test3()
test4()
test3()