import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n, m, k = pair()
arr = [list(pair()) for _ in range(n)]
v_max_info = []
h_max_info = []
res = []


for idx, line in enumerate(arr):
    if line[0] == 1:
        cur_len = 1
        start = 0
    else:
        cur_len = 0
        start = -1  
    for i in range(1, len(line)):
        if not line[i]:
            if cur_len >= k:
                h_max_info.append([idx, start, start+cur_len-1]) #y좌표, x좌표시작, x좌표끝
            cur_len = 0
            start = -1
        elif line[i-1] == 0 and line[i] == 1:
            start = i
            cur_len = 1
        else:
            cur_len += 1
    if cur_len >= k:
        h_max_info.append([idx, start, start+cur_len-1])
    cur_len = 0

for idx, line in enumerate([[i[j] for i in arr] for j in range(m)]):
    if line[0] == 1:
        cur_len = 1
        start = 0
    else:
        cur_len = 0
        start = -1  
    for i in range(1, len(line)):
        if not line[i]:
            if cur_len >= k:
                v_max_info.append([idx, start, start+cur_len-1]) #x좌표, y좌표시작, y좌표끝
            cur_len = 0
            start = -1
        elif line[i-1] == 0 and line[i] == 1:
            start = i
            cur_len = 1
        else:
            cur_len += 1
    if cur_len >= k:
        v_max_info.append([idx, start, start+cur_len-1]) #x좌표, y좌표시작, y좌표끝
    cur_len = 0

for i in h_max_info:
    for j in v_max_info:
        if j[0] in range(i[1], i[2]+1):
            res.append([i[0]+1, j[0]+1])

tot = 0
for line in arr:
    for i in line:
        tot += i

if res:
    print(len(res))
    for i in res:
        print(*i)
else:
    print(0)

"""
5 5 3
0 1 1 1 0
0 0 1 0 0
0 0 1 0 1
0 0 1 1 1
0 0 0 0 1


4 6 6
0 1 1 0 0 0
0 0 1 1 1 0
0 0 1 0 0 0
1 1 1 0 1 1

"""