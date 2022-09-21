import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = [list(pair()) for _ in range(n)]
dp = arr[0]

def solve(depth):
    global dp
    if depth == n:
        return
    tmp = list()
    for i in range(3):
        tmp2 = list()
        for j in range(3):
            if i == j:
                continue
            else:
                tmp2.append(arr[depth][i]+dp[j])
        tmp.append(min(tmp2))
    dp = list(tmp)
    solve(depth+1)

solve(1)
print(min(dp))

"""
점화식을 생각해보자...
i번째 집을 칠하는 최소 비용은
i-1번째 집을 칠할 때의 최소 비용과 i번째 집을 칠하는 최소 비용일까?

아니다. i-1번째 최소 비용에서 마지막 인덱스가 i번째 최소 비용의 인덱스와 같으면 안된다.
따라서 i-1번째에서의 최소 비용을 저장하는 것이 아니라
i-1번째의 모든 비용을 저장한 뒤 i번째에서는 
i-1의 1,2번 인덱스 최솟값 + i의 0번 인덱스 비용
i-2의 0,2번 인덱스 최솟값 + i의 1번 인덱스 비용

해서 총 2개씩 3회 비교하여 각각 i번째의 0,1,2번째 인덱스의 최솟값으로 한다.
"""