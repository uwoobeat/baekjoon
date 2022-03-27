import sys
import re
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
res = 0

t, g, f, p = s.count('T'), s.count('G'), s.count('F'), s.count('P')
cur = [0] * 4

def check():
    if cur[0]%3 == 0 and cur[1]%3 == 0 and cur[2]%3 == 0 and cur[3]%3 == 0:
        if sum(cur) >= 1:
            ccur = [0] * 4
            return True
    return False
        
def add_cur(letter):
    if letter == 'T':
        cur[0] += 1
    elif letter == 'G':
        cur[1] += 1
    elif letter == 'F':
        cur[2] += 1
    elif letter == 'P':
        cur[3] += 1

for i in range(len(s)):
    add_cur(s[i])
    if check():
        res += 1

print(res)