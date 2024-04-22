r = [1,2]
print(id(r))

r += [3,4]
print(id(r))


#id() = 해당 정보의 주소값, 값이 변경되어도 주소는 고정됨 (다만 튜플[ () ]은 저장하는 방식이 다르기에 주소가 변경됨)

t = (1,2)
print(id(t))
t += (3,4)
print(id(t))

def add_last(m, n):
    m += n 

r1 = [1,2]
add_last(r1, [3,4]) 
print(r1)

t1 = (1,2)
add_last(t1,(3,4)) #튜플은 절대로 추가안됨!!
print(t1)

def add_tuple(t1,t2):
    t1 += t2
    return t1

tp = (10,20)
tp = add_tuple(tp,(30,40))
print(tp)