import sys

def matrixMult(A):
    row=len(A)
    col=len(A[0])    
    
    B = [[0 for row in range(row)]for col in range(col)]
    
    for i in range(row):
        for j in range(col):
            B[j][i]=A[i][j]
    return B

stateArr = [['.','o','m','l','n'], ['o','w','l','n','.'], ['.','.','o','L','n']]

arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
transArr = matrixMult(arr)
row = len(arr[0])


for i in range(row):
    if transArr[i] == stateArr[0]:
        transArr[i] = stateArr[1]
    elif transArr[i] == stateArr[1]:
        transArr[i] = stateArr[0]

arr = matrixMult(transArr)

for i in range(5):
    for j in range(row):
        print(f"{arr[i][j]}", end = '')
    print("")