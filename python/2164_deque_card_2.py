#BOJ 2164 S4 deque_card_2

"""
deque을 활용해서 푸는 문제.
1. pop method가 기존 list의 pop method와 마찬가지로 삭제한 요소를 return한다는 점을 이용한다.
2. n=1 인 경우 반복문에서 첫번째 popleft 이후 두번째 실행문에서 pop할 요소가 없으므로 indexError가 발생한다.
따라서 while (1) 후 탈출 조건을 걸어주는 것이 아니라 while len(queue) > 1와 같이 처음부터 길이 조건을 고려한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i+1)


#solve 1 (indexError)

while 1:
    queue.popleft()
    queue.append(queue.popleft())
    if len(queue) <= 1:
        break

print(queue[0])


#solve 2

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())