x, y = [input() for _ in range(2)]

for i in reversed(y):
    print(int(x) * int(i))

print(int(x) * int(y))