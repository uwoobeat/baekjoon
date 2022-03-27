#BOJ 4673 self_number

def d(n):
    digitSum = sum(map(int, list(str(n))))
    return n + digitSum

numList = list(range(1,10000))

removeList = []

for i in numList:
    if d(i) < 10000:
        removeList.append(d(i))

for i in set(removeList):
    numList.remove(i)

for i in numList:
    print(i)
    
    