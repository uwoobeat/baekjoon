import sys

refArr = [[".", "o", "."], ["o", "w", "."], ["m", "l", "o"], ["l", "n", "L"], ["n", ".", "n"]]
arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
stateArr = [[] for _ in range(5)]
cnt = 0

print(arr)

for i in arr:
    for j in i:
        stateArr[cnt].append(refArr[cnt].index(j))
    cnt += 1

print(stateArr)

for i in range(5):
    for j in range(3):
        if stateArr[i][j] == 0:
            stateArr[i][j] = 1
        elif stateArr[i][j] == 1:
            stateArr[i][j] = 0

print(stateArr)

for i in range(5):
    for j in range(3):
        print(f"{refArr[i][stateArr[i][j]]}", end = '')
    print("")