#17829

"""
01
"""
import sys

def solve(arr, n):
    if n == 1:
        return arr[0][0]
    
    newArr = [[] for _ in range(n//2)]

    for i in range(0, n, 2):
        for j in range(0, n, 2):
            newArr[i//2].append(sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2])
    
    return solve(newArr, n//2)

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solve(arr, n))