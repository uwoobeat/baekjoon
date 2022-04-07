import sys

input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
arr = list(pair())
dp = [-1] * n #가능한 최대 박스 갯수를 저장하는 dp 배열 선언

for i in range(n):
    cur = 0 #현재 가능한 최대 박스 갯수
    for j in range(i):
        if arr[i] > arr[j]: #i의 값이 돌고 있는 값보다 크면
            cur = max(cur, dp[j]) #현재 가능한 최대 박스 갯수를 dp 저장값과 비교하여 갱신.
    dp[i] = cur + 1 

print(max(dp))
"""
박스 갯수인 cur + 1을 dp에 저장한다.
cur + 1이 항상 성립하는 이유는
1은 i번째 박스이고 cur은 arr[i]보다 작을 때의 최대 가능 개수이므로 dp[i]에는 항상 cur+1이 가능하다.
"""