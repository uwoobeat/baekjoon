"""
우유 8 노른자 8 설탕 4 소금 1 밀가루 9 -> 반죽 16
x배의 재료에 대해 [16x]개의 반죽 획득(가우스?)

바나나 -> 바나나 1
딸기 -> 딸기30
초콜릿 -> 초콜릿 25
호두 -> 호두 10

바나나는 여러 조각으로 나눌 수 있다.
"""

import math

N = int(input())

for _ in range(N):
    _ = input()
    milk, egg, sugar, salt, flour = map(int, input().split())
    banana, straw, choco, hodu = map(int, input().split())
    dough = math.floor(16 * min(milk / 8, egg / 8, sugar / 4, salt, flour / 9))
    topping = banana + straw // 30 + choco // 25 + hodu // 10
    print(min(dough, topping))