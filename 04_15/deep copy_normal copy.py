# == 은 내용물이 같은지 조사하는거
# is 는 서로 참조하는 객체가 같은가

r1 = [1,2,3]
r2 = []
r3 = [1,2,[3,4]]

r4 = list('hello')
r5 = list((6,7,8))
r6 = list(range(0,5))

print(r4,r5,r6)


n1 = [1,2,3,4,5]
n2 = [x * 2 for x in n1]

print(n2)