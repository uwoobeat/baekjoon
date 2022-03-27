#5525 IOIOI

import sys
input = sys.stdin.readline

n, m = map(int, [input().rstrip() for _ in range(2)])
pstr = input().rstrip()
find = "I" + "OI" * n
cnt = 0

while (1):
    if find in pstr:
        pstr = pstr[pstr.find(find)+1:]
        cnt += 1
    else:
        break

print(cnt)

#sol 2

import sys
input = sys.stdin.readline

n, m = map(int, [input().rstrip() for _ in range(2)])
s = input().rstrip()

i = 1
cnt = 0
res = 0

while i < m -1:
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