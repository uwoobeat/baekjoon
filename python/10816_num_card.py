import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

res = dict()

for i in nlist:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

for i in mlist:
    if i in res:
        print(res[i], end = ' ')
    else:
        print(0, end = ' ')