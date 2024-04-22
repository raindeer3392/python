name = 'name'
age = 0
member = {}

def show_member(name):
    global member
    print("\n\n\n이름:", name, "\n나이:", member[name])

def add_member(name,age):
    global member
    member[name] = age

def main():

    name = input("이름 입력:")
    age = input("나이 입력:")

    add_member(name,age)

    show_member(input("꺼내올 사람:"))



main()