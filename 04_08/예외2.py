def main():
    while True:
        try:
            age = int(input("나이입력"))
            print(age)
            break
        except ValueError:
            print("입력이 잘못되었습니다. 다시 입력해주세요.")

    print("끝")

main()