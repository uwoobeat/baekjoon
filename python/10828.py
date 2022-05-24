import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())
arr = list()

def push(arr, x):
    arr.append(x)

def pop(arr):
    if arr:
        return arr.pop()
    else:
        return -1

def size(arr):
    return len(arr)

def empty(arr):
    if arr:
        return 0
    else:
        return 1

def top(arr):
    if arr:
        return arr[-1]
    else:
        return -1

for _ in range(int(input())):
    cmd = input()
    if "push" in cmd:
        _, num = cmd.split()
        push(arr, num)
    elif cmd == "pop":
        print(pop(arr))
    elif cmd == "size":
        print(size(arr))
    elif cmd == "empty":
        print(empty(arr))
    elif cmd == "top":
        print(top(arr))