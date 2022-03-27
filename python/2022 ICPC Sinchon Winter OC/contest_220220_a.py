import sys
input = sys.stdin.readline

c = int(input())
res = 0

for _ in range(c):
    string = input().rstrip()
    tmp = 0
    i = 0
    while i <= len(string)-3:
        if string[i:i+3] == "for":
            i += 3
            tmp += 1
        elif string[i:i+5] == "while":
            i += 5
            tmp += 1
        else:
            i += 1
    if tmp > res:
       res = tmp

print(res)