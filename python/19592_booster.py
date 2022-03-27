#BOJ 19592 S5 toy_race

"""
초등학교 수학 문제지만 코드로 구현하는 것은 나름 어렵다... 보기 좋게 짜는 것도 어렵다...
굳이 math 모듈을 썼어야 할까?
"""
import math

T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))
    
    velocity = V.pop(N-1)
    time = X / max(V)
    Z = X - (time - 1) * velocity
    if Z.is_integer(): #little bit messy?
        Z += 1
        Z = int(Z)
    else:
        Z = math.ceil(Z)

    if X / velocity < time:
        print(0)
    elif Y < Z:
        print(-1)
    else:
        print(Z)