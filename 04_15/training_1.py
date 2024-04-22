num = 0

def add_one(): # 플러스 1
    global num #num의 값을 이 함수 외에서도 적용되게 함
    num += 1 #기존 num값 + 1

def minus_one(): # 마이너스 1
    global num #num의 값을 이 함수 외에서도 적용되게 함
    num -= 1 #기존 num값 - 1

def show_num(): #숫자 보여주기
    global num #num의 값을 이 함수 외에서도 적용되게 함
    print('현재 값:', num)

def main():
    global num #num의 값을 이 함수 외에서도 적용되게 함
    while True: #종료될때까지 반복함
        show_num()
        select = int(input('1 더하기:1, 1 빼기:2, 종료:3 \n동작 선택:')) #터미널에 질문해서 입력값을 받음
        if select == 1: #입력값이 1일때 add_one()을 실행함
            add_one()

        elif select == 2: #입력값이 2일때 minus_one()을 실행함
            minus_one()

        elif select == 3: #입력값이 3일때 show_num()을 실행함
            show_num()
            print("끝")
            break #종료
        

main() #프로그램 실행