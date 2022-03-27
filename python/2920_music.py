#BOJ 2920 B2 music

"""
아니 진짜로 12345678 87654321만 판별하면 되는거임? 킹받네
23456781도 되는거 아님?
"""
lst = list(map(int, input().split()))
count = 0
order = ""

note = list(lst)
check = 0

for i in range(len(note) - 1):
    if note[i] == 8:
        note[i] = 0
    if not note[i+1] - note[i] == 1:
        check += 1
if check == 0:
    order = "ascending"

note = list(lst)
check = 0

for i in range(len(note) - 1):
    if note[i+1] == 8:
        note[i+1] = 0
    if not note[i] - note[i+1] == 1:
        check += 1
if check == 0:
    order = "descending"

if not order:
    order = "mixed"

print(order)


"""
문제에서 원했던 풀이
"""
note = list(map(int, input().split()))

if note == sorted(note):
    print("ascending")
elif note == list(reversed(note)): #or sorted(note, reverse = True)
    print("descending")
else:
    print("mixed")