"""
(x,y,z)에서 x->y->z로 갈수록 깊이를 1씩 증가시킨다.

dfs이므로 1->1->1,2,3, 1->2->1,2,3 ...

최대 깊이에 도달하면 출력 후 반환. 이후 마지막 깊이의 숫자 지우고 +1 하여 반복.

1) for문 진입하면 해당 수 추가
2) 재귀하여 다음 깊이의 수 추가
3) 최대 깊이이면 삭제하고 +1 하여 반복

dfs 함수의 매개변수로 depth, n, m 둬도 되지만 전역변수처럼 다룬 후 dfs()와 같이 풀이하는 것도 가능
"""

n, m = map(int, input().split())

s = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return
    for i in range(n):
        s.append(i+1)
        dfs(depth+1, n, m) 
        s.pop()
        
dfs(0, n, m)