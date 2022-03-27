#15401 S5

"""
https://youtu.be/b4sYvdc9UeU

이진 탐색
하이로우 게임을 생각하면...
무조건 중간값을 부르자(소수점은 버리고)
0~100에서 68 찾기 : 50 up, 75 down, 62 up, 68 정답
상한선과 하한선을 좁혀가면서, 그 중간값을 정답으로 수렴시키는 방식...

이걸 문제에 적용해보자.
왜 이진 탐색을 쓰는가? 탐색 범위가 20억. 브루트포스로 풀면 무조건 시간초과
하지만 10억/2^29 = 1.x, /2^30 = 0.x. 이진탐색으로 30번 돌면 무조건 풀린다
기하급수적으로 줄어드므로, 편리하다!

3명 [8 7 6 5 4 3 2 1]
과자 최대 길이 8 최소 길이 0
0~8에서 3명 가능한지 확인하기 : 4 yes(2->3->break), 6 yes(), 7 no -> 6
1 2 3 4 5 6 7 8
mid = 4, 0,0,0,1,1,1,1,2로 6명.
mid = (5+8)//2 = 6, 0000111 = 3명으로 가능.
mid = 7+8//2 = 7, 00000011 = 2명로 불가능. 답은 3

0~10이면 mid = 5, cnt = 4
6~10이면 mid = 8, cnt = 3
9~10이면 mid = 9, cnt = 2
9~8이면 break

1~10이면 mid = 5일 때도 마찬가지. 따라서 start = 1이여도 상관없다.
0인 예외를 고려해주는 것보다는, 사이클을 돌지 않았을 경우 0이라고 판단하는 것이 좋다.
이를 위해서 기본값을 0로 설정해주는 것. zdv error를 피하기 위해 start = 1로 설정했다. 결과는 차이 없음.
"""


import sys

m, n = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

start = 1 #avoiding zerodivision error
end = max(lst)
result = 0

while (start <= end):
    mid = (start + end) // 2
    cnt = sum([i//mid for i in lst])
    if cnt >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1 #set breakpoint: end -1 

print(result)