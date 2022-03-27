#15649 S3 N&M_1

"""
1~N까지 중 중복 없이 M개 고르기

백트래킹과 DFS를 이용한다. 백트래킹에 사용되는 것이 DFS이다.
DFS는 대개 재귀함수로 구현한다.
for문 중첩을 통해 depth를 구현할 수는 있지만 탐색 횟수(a.k.a 시간 복잡도)가 많이 차이난다.
(= 공통 상위의 리프 노드를 고려하지 않기에)
또한 탐색 과정에서의 컨트롤도 불가능하다.
따라서 탐색 역할을 수행하는 함수를 재귀호출하여 depth를 하나씩 증가시키는 쪽으로 이용한다.
이렇게 하면 재귀 호출이 끝났을 때 for문처럼 완전히 다시 시작하는 것이 아니라,
이전 층위의 탐색 상태를 유지하면서 다른 노드를 탐색할 수 있다.

처음 풀이 - 각 층위에 해당하는 visitList를 각각 생성해주었다.
나중 풀이 - 하나의 visitList를 사용하되, 탐색 종료 후 출력 시 마지막 결괏값과 방문 여부를 초기화한다. 
"""

N, M = map(int, input().split())

visitList = [0] * N
result = []

def visit(depth):
    if depth == M: #M-1일 것 같지만, 0~M-1까지가 M개이고 depth가 M일 때는 M-1까지 스택이 쌓인 것이므로 맞다. 
        print(*result) #unpacking
    for i in range(N):
        if not visitList[i]:
            visitList[i] = 1
            result.append(i + 1)
            visit(depth + 1)
            result.pop()
            visitList[i] = 0

visit(0)