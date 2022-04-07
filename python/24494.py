import sys

input = sys.stdin.readline
pair = lambda : map(int, input().split())

ans = sum([list(input().rstrip()) for _ in range(3)], [])
guess = sum([list(input().rstrip()) for _ in range(3)], [])
check = []
green = 0
yellow = 0

for i in range(9):
    letter = guess[i]
    if letter in ans:
        if letter == ans[i]:
            green += 1
        else:
            if letter not in check:
                check.append(letter)
                yellow = guess.count(letter)

print(green)
print(yellow-green)

#WA