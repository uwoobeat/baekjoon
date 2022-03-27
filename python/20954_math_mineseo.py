"""
1. x좌표가 2의 몇승인지 확인한다.
2. Di의 리스트를 만든다.
3. 원소 간 탐색 범위 사이에 x가 존재하는지 확인한다.
4. 있다면 원소 간격 범위를 x로 하고 해당 간격을 추가하여 종료한다.
"""

import sys
import math

T = int(input())
lst = map(int, [sys.stdin.readline() for _ in range(T)])

for x in lst:
    time = 0
    i = 0
    num1 = 0
    while True:
        num2 = ((-1) ** i) * (2 ** math.floor(i / 2))
        if not num1 <= abs(x) <= num2 or num2 <= abs(x) <= num1: 
            time += abs(num2 - num1)
            num1 = num2
            i += 1
        else:
            time += abs(x - num1)
            break
    print(time)
    