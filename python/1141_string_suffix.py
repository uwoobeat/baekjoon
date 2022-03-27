import sys
input = sys.stdin.readline


def compare_prefix(str1, str2):
    check = True
    strlen = len(str1)
    for i, j in zip(str1, str2):
        if i == j:
            continue
        else:
            return False
    return True

n = int(input())
lst = sorted([input().rstrip() for _ in range(n)], key = len)


for i in lst:
    index = lst.index(i)
    word = lst.pop(index)
    check = 0
    for j in lst[index:]:
        if check:
            break
        if compare_prefix(word, j):
            check = 1
    if not check:
        lst.insert(index, word)

print(lst)
"""
for i in range(n-1):
    word = lst.pop(i)
    check = 0
    for j in lst:
        if word in j:6
hello
hi
h
run
rerun
running
            check = 1
    if not check:
        lst.insert(i, word)

print(lst)
"""


"""
for i in range(n):
    word = lst.pop(i)
    for j in lst:
        if word in j:
            check += 1
"""
"""
h hello hi rerun run running
h -> hello hi 안됨, rerun run running 됨
hello -> hi, rerun, run running 됨
hi -> rerun, run, running 됨
rerun -> run running 됨
run -> running 안됨

h로 시작
h rerun run running -> get
hello 시작
hello hi rerun run running -> get
hi -> pass
rerun -> pass
run -> pass

hello hi rerun run running
hi -> rerun run running 됨
rerun -> 됨
run -> running 안됨
hello hi rerun run 4개
"""

"""
a b cba cbb cbc ccc
a -> 다됨, 6개
b -> 다됨, 6개
cbc -> 다됨
cbb -> 다됨

전부 다 되므로 6개

즉 하나를 뽑았을 때 나머지 원소에 대하여 접두사 여부 비교하여 나누고,
모든 원소에 대해 접두사 아닌 리스트의 길이 비교하여 최대길이인 것 고르기
만약 최대 길이에 포함된 원소에 대해서 해당 원소의 접두사 X 리스트에 다른 원소가 포함된다면 
"""