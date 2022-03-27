# 1182 S2 part_arr_sum

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def dfs(index, res):
    global cnt
    if index == n:
        if res == s:
            cnt += 1
        return
    dfs(index+1, res)
    dfs(index+1, res+arr[index])

dfs(0, 0)
print(cnt if s != 0 else cnt-1)