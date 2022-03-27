#BOJ 8958 OX

N = int(input())
lst = [input() for _ in range(N)]

for result in lst:
    count = 0
    score = 0
    
    for i in result:
        if "O" == i:
            count += 1
            score += count
        if "X" == i:
            count = 0
    print(score)
    