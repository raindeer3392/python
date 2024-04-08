import module_stu

def main():
    r = float(input("반지름 :"))

    ar =  module_stu.Area_C(r)
    print("넓이 :", ar)
    ci = module_stu.Circum_C(r)
    print("넓이: ", ci)


main()