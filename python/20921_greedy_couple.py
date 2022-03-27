import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(n, 0, -1))
case = [0] * n
cnt, index = 0, 0

while arr:
    if k >= len(arr[cnt+1:]):
        k -= len(arr[cnt+1:])
        case[index] = arr[cnt]
        index += 1
        arr.pop(cnt)
        cnt = 0
    else:
        cnt += 1

print(*case)


"""
4, 2
1번 자리에 들어가면 3자리 남고 4 들어가면 3개 생김
1번 자리에 들어가면 3자리 남고 3 들어가면 2개 생김 -> get, [3,0,0,0], k -= 2이면 k=0
2번 자리에 들어가면 2자리 남고 4 들어가면 2개 생김
2번 자리에 들어가면 2자리 남고 2 들어가면 1개 생김
2번 자리에 들어가면 2자리 남고 1 들어가면 0개 생김 -> get, [3,1,0,0]
3번 자리에 ~ 4 들어가면 1개 생김
3번 자리에 ~ 2 들어가면 0개 생김 -> get, [3,1,2,0]
4번 자리에 4 들어가면 0개 생김 -> get, [3,1,2,4]
"""