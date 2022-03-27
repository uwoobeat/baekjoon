import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n, m = pair()
matrix = [list(input().rstrip()) for _ in range(n)]
checkList = [[1] * m for _ in range(n)] #반복 비교를 막기 위한 부분체크판 충족 여부
res = n * m
k = 2

while k <= min(n, m):
    line1 = ["W" if i%2 else "B" for i in range(k)]
    line2 = ["B" if i%2 else "W" for i in range(k)]
    board1 = [line2 if i%2 else line1 for i in range(k)] #b로 시작하는 부분체스판
    board2 = [line1 if i%2 else line2 for i in range(k)] #w로 시작하는 부분체스판
    for i in range(n-k+1): #x축 이동
        flag = False #2중 for문 탈출 위한 변수
        for j in range(m-k+1): #y축 이동. 좌표는 matrix[j][i] 형태임
            if checkList[j][i] == 0: #이전 부분체스판 비교에서 거짓이라면 그보다 큰 체스판에서도 거짓임
                flag = True
                break
            
            start = matrix[j][i]
            check = 1            
            
            if start == "B":
                for y in range(k):
                    flag2 = False
                    for x in range(k):
                        if matrix[j+y][i+x] != board1[y][x]:
                            flag2 = True
                            check = 0
                            checkList[j+y][i+x] == 0
                            break
                    if flag2:
                        break

                    
            elif start == "W": #W로 시작하는 보드와 일치 여부 비교
                for y in range(k):
                    flag2 = False
                    for x in range(k):
                        if matrix[j+y][i+x] != board2[y][x]:
                            flag2 = True
                            check = 0
                            checkList[j+y][i+x] == 0
                            break
                    if flag2:
                        break
            if check:
                res += 1

        if flag:
            break
    k += 1

print(res)
"""
1. 반복문마다 nxn 크기의 체스판을 만들고 확인한다.
2. 만약 불가능하면 불가능 리스트에 해당 체스판의 좌상단 좌표를 기록한다.
3. 다음 n+1 x n+1 순회에서는 불가능 리스트에서 시작점을 확인하고 비교 여부를 결정한다.
"""

"""
새로운 비교 알고리즘
이전 문자를 tmp에 저장하고 만약 다음 문자가 이전 문자와 같은 경우 체스판 x 판정
=> 새로운 비교용 체스판을 만들 필요가 없으니 이득임
"""