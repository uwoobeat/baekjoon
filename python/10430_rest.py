x = input()
numlist = x.split()

A = int(numlist[0])
B = int(numlist[1])
C = int(numlist[2])

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print((A%C)*(B%C)%C)