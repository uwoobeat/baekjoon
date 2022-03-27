import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = sorted([input().rstrip() for _ in range(n)])
    slen = len(lst)
    check = 0
    for i in range(slen-1):
        if lst[i] == lst[i+1][:len(lst[i])]:
            check = 1
            break
    print("YES") if not check else print("NO")