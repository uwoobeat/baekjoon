import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

s = input()
u = s.count("U")
d = s.count("D")
p = s.count("P")
c = s.count("C")
uc = u + c
dp = d + p

res = ""
flag = False

if uc > (dp + 1) // 2: # uc를 u로 바꾸고 dp를 절반으로 쪼개면 됨. 홀수만 잘 처리
    res += "U"
    flag = True
if dp > 0: # 존재하기만 하면 uc를 c로 바꾸면 됨
    res += "DP"
    flag = True
if not flag:
    res += "C"

print(res)