#BOJ 3052

lst = []
count = 0

for _ in range(10):
    lst.append(int(input()))

lst = list(map(lambda x : x % 42, lst))

print(len(set(lst)))
