"""
1~N 총 N개 있음
k시간마다 추가 결제. K시간마다 C원씩내야 함. 즉 T*K초일 때 T*C원 내야 함

선풍기 500원 3시간마다 100원, 12시간
단, 집에 도착하면 발생 안하고 선풍기 끈다. (마지막 단위 전 도착이면 카운트 안함)

12 // 3 = 4

100원 2시간마다 누진 100원
200원 3시간마다 누진 100원
0원 10시간마다 누진 500원
0원 10시간마다 600원
1000원 13시간마다 100원

5개, 12시간이면?
-> 100+500
-> 200+300
-> 0+500
-> 0+600
-> 1000

나머지 남는 것 / 안남는 것 / 몫 0인 것 (나머지 남음) 
"""

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
min_cost = 2 ** 63 - 1
res = 0

for i in range(n):
    p, k, c = map(int, input().split())
       
    if q // k > 0:
        if q % k == 0:
            p += (c + c * (q // k - 1)) / 2 * (q // k - 1)
        else:
            p += (c + c * (q // k)) / 2 * (q // k)
    
    if p < min_cost:
        min_cost = p
        res = i+1

print(res, int(min_cost))