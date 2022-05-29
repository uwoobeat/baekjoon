import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

n = int(input())
arr = [0] * 100001 #인덱스를 출력하는 것이므로 +1 연산을 추가하는 과정에서 메모리가 더 사용된다

for _ in range(n):
    arr[int(input())] += 1

for i in range(10001):
    if arr[i]:
       for j in range(arr[i]):
           print(i)

"""
pypy3가 아닌 python 3를 통해 채점한다.
간단한 반복 연산의 경우 pypy3보다 python3가 더 빠르다.
반면 복잡한 반복 연산의 경우 (for-if-else) pypy3가 더 빠르다.

또한 [print(i) for _ in range(arr[i])]와 같이 컴프리헨션을 사용하면 메모리 초과가 난다.
많은 양의 수를 입출력할 때는 파이선의 기초적인 기능을 이용하도록 하자.
"""