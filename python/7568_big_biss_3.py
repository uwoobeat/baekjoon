import sys
input = sys.stdin.readline

n = int(input())
sizeList = [list(map(int, input().split())) for _ in range(n)]
rankList = [0] * n
index = 0

for size in sizeList:
    rank = 1
    for i in range(n):
        if size[0] < sizeList[i][0] and size[1] < sizeList[i][1]:
            rank += 1
    rankList[index] = rank
    index += 1

print(*rankList)
        

"""
1위부터 시작
55 185
1
58 183
키 크고 몸 작음 - 2 2
88 186
키 크고 몸 큼 2 2 1
60 175
키 작고 
"""