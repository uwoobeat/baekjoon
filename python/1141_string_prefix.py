import sys
input = sys.stdin.readline

def compare_prefix(str1, str2):
    check = True
    strlen = len(str1)
    for i, j in zip(str1, str2):
        if i == j:
            continue
        else:
            return False
    return True

n = int(input())
lst = sorted([input().rstrip() for _ in range(n)], key = len)
res = 0

for i in range(n):
    word = lst[i]
    check = 0
    for j in lst[i+1:]:
        if check:
            break
        if compare_prefix(word, j):
            check = 1
    if not check:
        res += 1

print(res)