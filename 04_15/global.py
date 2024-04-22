num1 = 100

def test():
    num1 = 10
    print(num1)

test()
print(num1)

def test():
    global num1
    num1 = 10
    print(num1)

test()
print(num1)