import sys

"""
.o..o
ow..w
mlool
lnLLn
n.nn.
"""
def matrixMult(A):
    row=len(A)
    col=len(A[0])    
    
    B = [[0 for row in range(row)]for col in range(col)]
    
    for i in range(row):
        for j in range(col):
            B[j][i]=A[i][j]
    return B


refArr = [['.', 'o'], ['o', 'w'], ['.', '.']]

arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
transArr = matrixMult(arr)
refArr = matrixMult(arr)
stateArr = [2] * len(arr[0])
row = len(arr[0])

print(arr)
print(state_ref_arr)

for i in range(row-1):
    for lst in refArr:
        if transArr[i] == :
            stateArr[i] = refArr.index(lst)

for i in range(row):
    if stateArr[i] == 0:
        stateArr[i] = 1
    elif stateArr[i] == 1:
        stateArr[i] = 0

for i in range(5):
    for j in range(row):
        print(f"transArr[stateArr[j]][i]}", end = '')
    print("")