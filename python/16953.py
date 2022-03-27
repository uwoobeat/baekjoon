import sys

input = sys.stdin.readline
pair = lambda : map(int, input().split())

cnt = 0

def solve(x, y):
    global cnt
    if x == y:
        return cnt+1
    elif y % 10 == 1:
        solve(x, y//10)
        cnt += 1
    elif y % 2 == 0:
        solve(x, y//2)
        cnt += 1
    else:
        return -1

x, y = pair()
solve(x, y)
print(cnt+1)

"""
끝자리가 1 -> 10으로 나눈 몫을 반환
짝수라면 -> 2로 나눈 몫을 반환
"""