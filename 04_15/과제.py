n1 = [2,3,4,5,6,7,8,9]
n2 = [1,2,3,4,5,6,7,8,9]

r = [x * y for y in range(1,10) for x in range(2,10) if (x * y)%2]
print(r)