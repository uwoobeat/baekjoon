import sys
input = sys.stdin.readline

n, m = map(int, [input().rstrip() for _ in range(2)])
s = input().rstrip()

i = 1
cnt = 0 #n count
res = 0

while i < m - 1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I":
        cnt += 1
        if cnt == n:
            res += 1
            cnt -= 1
        i += 1
    else:
        cnt = 0
    i += 1

print(res)