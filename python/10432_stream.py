import sys
input = sys.stdin.readline
p = int(input())

for i in range(p):
    arr = list(map(int, input().split()))
    plst = [0] * 13
    depth, end, cnt = 0, 0, 0
    for j in range(1, 12):
        if arr[j] > end:
            depth += 1
            cnt += 1
            plst[depth] = arr[j]
        elif arr[j] < end:
            while arr[j] < plst[depth] and depth > 0:
                depth -= 1
        if arr[j] > plst[depth]:
            depth += 1
            cnt += 1
            plst[depth] = arr[j]
        end = arr[j]     
    print(i+1, cnt)