import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x, y = map(int, sys.stdin.readline().split())

cnt_x = int(n * x / 100)
cnt_y = 0

for i in arr:
    if i >= y:
        cnt_y += 1
        
print(f"{cnt_x} {cnt_y}")