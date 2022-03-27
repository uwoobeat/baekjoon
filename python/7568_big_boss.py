#7568 - big boss

N = int(input())
sizeList = []
rankList = [0] * N
index = 0

for _ in range(N):
    weight, height = map(int, input().split())
    sizeList.append([weight, height])
    

print(sizeList)
print(rankList)

for size in sizeList:
    count = 1
    for i in range(N):
        if sizeList[i][0] > size[0] and sizeList[i][1] > size[1]:
            count += 1
    rankList[index] = count
    index += 1

print(' '.join(list(map(str, rankList))))