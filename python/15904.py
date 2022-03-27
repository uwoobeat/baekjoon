import sys
input = sys.stdin.readline

s = input().rstrip()
ans = list("UCPC")
cnt = 0
checkList = [0] * 4

for letter in s:
    if cnt > 3:
        break
    if letter == ans[cnt]:
        checkList[cnt] = 1
        cnt += 1

if sum(checkList) == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")