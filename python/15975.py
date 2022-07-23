import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

def distance(a):
    leng = 0 
    for i in range(len(a)):
        if i == 0:
            leng += abs(a[i] - a[i + 1])
        elif i == len(a) - 1:
            leng += abs(a[i] - a[i - 1])
        else:
            leng += min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]))
    return leng

n = int(input())
ans = 0
arr = []
for _ in range(n):
    x,y = pair()
    arr.append([y, x])
arr.sort()
colorCount = arr[-1][0]

for i in range(1, colorCount+1):
    pos = []
    for j in range(n):
        if arr[j][0] == i:
            pos.append(arr[j][1])
    ans += distance(pos)

print(ans)