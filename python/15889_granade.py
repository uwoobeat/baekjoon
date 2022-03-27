import sys
input = sys.stdin.readline

n = int(input())
posList, rangeList = [list(map(int, input().split())) for _ in range(2)]
dis = 0

for i in range(n-1):
    dis = max(dis, posList[i] + rangeList[i])
    if dis < posList[i+1]:
        print("엄마 나 전역 늦어질 것 같아")
        exit()
        
print("권병장님, 중대장님이 찾으십니다")