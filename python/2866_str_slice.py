#2866 G5 string_slice

import sys
input = sys.stdin.readline

def is_dup_check(lst):
    return sorted(lst) != sorted(list(set(lst)))

r, c = map(int, input().split())
lst = [list(input().rstrip()) for _ in range(r)]
start, end, cnt = 0, r-1, 0

while start <= end:
    mid = (start + end) // 2
    slst = [''.join([lst[i][j] for i in range(mid, r)]) for j in range(c)]
    
    if is_dup_check(slst):
        end = mid - 1
    else:
        start = mid + 1
    
print(start-1)

"""
for _ in range(r):
    del lst[0]
    r -= 1
    slst = [''.join([lst[i][j] for i in range(r)]) for j in range(c)]
    
    if is_dup_check(slst):
        print(cnt)
        exit()
    else:
        cnt += 1
"""