import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, m, k = pair()
tot = 0
arr = []
pos = []

for _ in range(n):
    line = list(pair())
    tot += sum(line)
    arr.append(line)

varr = [[i[j] for i in arr] for j in range(m)]

print(arr)
print(tot)

if tot == k*2:
    print(0)
elif tot == k*2-1:

    for idx, line in enumerate(arr):
        line_sum = sum(line)
        if line_sum == 2*k-1:
            pos.append((idx, line.index(1)+k-1))
            break
        elif line_sum == k:
            for i in 
            pos.append((idx, line.index(1)))
            break
    
    for idx, line in enumerate(varr):
        line_sum = sum(line)
        if line_sum == 2*k-1:
            pos.append((line.index(1)+k-1, idx))
            break
        elif line_sum == k:
            pos.append((line.index(1), idx))
            break
else:
    dup_cnt = 2*k - tot

    for idx, line in enumerate(arr):
        line_sum = sum(line)
        if line_sum == tot:
            for _ in range(dup_cnt):
                pos.append((idx, line.index(1)+(tot-dup_cnt)/2))
            
print(len(pos))
for i in pos:
    print(f"{i[0]+1} {i[1]+1}")