import sys
input = sys.stdin.readline
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]
prized = []

for i in range(1,5):
    score = [arr[k][i] for k in range(n)]
    max_score = max(score)
    idxList = [k for k,v in enumerate(score) if v == max_score]
    numList = [arr[x][0] for x in idxList]
    std_num = min(numList)
    prized.append(std_num)
    arr.pop(idxList[numList.index(std_num)])
    n -= 1

print(*prized)
"""
과목별 1등이 상
인당 상 1번씩
국영수탐 순으로 상

국 영 수 탐 순으로 확인하되
상을 탄 인원의 값을 제거해버리자
"""