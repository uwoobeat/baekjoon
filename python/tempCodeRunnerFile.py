
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

print(dp)