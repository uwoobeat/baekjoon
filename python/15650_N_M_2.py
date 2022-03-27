#15650 S3 N_M_2

N, M = map(int, input().split())

visitList = [0] * N
result = []
temp = []

def visit(depth):
    global temp
    
    if depth == M:
        if result == sorted(temp) or temp == []:
            print(*result)
            temp = result
    for i in range(N):
        if not visitList[i]:
            visitList[i] = 1
            result.append(i + 1)
            visit(depth + 1)
            result.pop()
            visitList[i] = 0

visit(0)