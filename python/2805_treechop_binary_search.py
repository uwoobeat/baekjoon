"""
이진 탐색

1) 처음 <= 끝일 때까지 반복
2) 결과값이 목표치더라도 한번 더 반복하여 경계조건 확정
3) 마지막 반복 후 경계 넘지 않으면 다시 반복,
4) 만약 넘었다면 끝 = 중간 - 1하여 끝을 이전 반복의 중간값으로 할당 & 끝이 처음보다 작아지므로 반복문 조건 빠져나감

2)와 4)의 아이디어를 눈여겨보자.
경계조건을 확정짓는 논리와 해당 값을 별도의 break 없이 처리하는 방법이 핵심. 
"""

_, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

while (start <= end):
    mid = (start + end) // 2
    result = 0
    
    for i in arr:
        if i > mid:
            result += i - mid
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)