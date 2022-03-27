import sys

N = int(input())
lst = []
end = 0
count = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a,b))

lst.sort(key = lambda x: (x[1], x[0]))

for i,j in lst:
    if i >= end:
        end = j
        count += 1

print(count)