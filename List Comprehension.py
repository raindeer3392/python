#GPT로 알고리즘 이해한 식

def yaksu(number):
    return [i for i in range(1,number + 1) if number % i == 0] 

# 1~19의 i를 number로 나누었을때 맞아 떨어지는 i값을 반환함

yaksu_18 = yaksu(18)
yaksu_24 = yaksu(24)

#각 수의 약수



#filter 함수 사용
sippal = list(range(1,19))
ys_18 = list(filter(lambda n: not(18 % n), sippal))

print('ys_18')

#점검

#list_comprehension 함수 사용
yisipsa = list(range(1,24))
ys_24 = [n for n in yisipsa if not(24 % n)]

print('ys_24')
#점검

#대충 이렇게 하면 이해했으니 공약수나 만듭시다

gys1 = [i for i in range(1, 25) if not(18 % i) and not(24 % i)]
gys2 = list(filter(lambda n: not(18 % n) and not(24 % n), range(1,25)))

print(gys1)
print(gys2)