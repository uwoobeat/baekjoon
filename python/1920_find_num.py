import sys
input = sys.stdin.readline

_ = input()
nlist = list(map(int, input().split()))
_ = input()
mlist = list(map(int, input().split()))

for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)