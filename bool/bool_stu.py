True

print(type(True))
# - bool = 부울형 데이터 , 참과 거짓으로 신호를 줌


print(3==5)

if (3<10):
    print("테스트용")

if 3<10:
    print("테스트용")

not print("테스트2")

# if문, if에 괄호를 안넣어도 작동은 하는듯?
# if문에 else도 되고 not도 되는건가? 아니면 익스텐션인가?

''
def some():

    test = int(input("받아봄"))

    if test<10:
        print("작다")
    elif test<10:
      print("크다")
    else:
        print("뭐냐")

some()

# if문에는 총 3개를 작성할수 있는데
# if로 먼저 처음 받아보고 맞으면 그대로 출력
# 근데 처음 질문이 폴스값이 나오면 elif, else if 문으로 b플랜을 시도함
# 근데 b플랜도 실패한다? else로 모든게 실패했을때의 결과값을 제공