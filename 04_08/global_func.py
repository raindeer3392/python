fa_age = 39

def up_fa_age():
    global fa_age
    fa_age += 1

def get_fa_age():
    return fa_age

def main():
    print("올해 아빠 나이:", get_fa_age())
    up_fa_age()
    print("내년 아빠 나이:", get_fa_age())

main()