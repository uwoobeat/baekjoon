import sys

input = lambda: sys.stdin.readline().rstrip()

s1 = input()
s2 = input()
s1_len = len(s1)
s2_len = len(s2)
dp = [[0] * (s2_len+1) for _ in range(s1_len+1)]

for i in range(1, s1_len+1):
    for j in range(1, s2_len+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

"""
웰노운 == 모르면 맞아야지

dp[i][j] : 수열 s, t에 대해 s의 i번째 수, t의 j번째 수를 통틀어 lcs라고 가정
dp[i][j] = max(dp[i-1][j], dp[i][j-1])인데 여기에 의미있는 문자가 추가된 경우라면

dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + int(s1[i]==s2[j]))

+ 재귀, 문자열 한정으로 python3를 사용하는 것이 좋다 (재귀쓰면 메모리 터짐)
++ python3는 내장함수보다 if-else를 통한 처리가 더 빠르다
+++ pypy3는 python3보다 내장함수 속도가 더 빠르다
"""