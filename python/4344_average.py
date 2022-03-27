#BOJ 4344

C = int(input())

for _ in range(C):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    count = 0
    average = sum(lst) / N
    for i in lst:
        if i > average:
            count += 1
    print(f"%.3f%%" %(count / N * 100)) #"%%" is needed to print "%" in prinf-formatting