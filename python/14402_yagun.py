"""
들어간 기록은 없는데 나온 기록 있음 -> 야근 (+ 없이 -, 즉 --)
들어갔는데 나온 기록 없음 -> 야근 (+ 있는데 - 없음. 즉 ++)
둘 다 -> 야근 두번
나오거나 들어가지 않음 -> 야근 아님
이름이 같음 -> 같은 사람

+ - - - + + +는
들어감 나옴 나옴(+1) 나옴(+1) 들어감(+1) 들어감(+1) 들어감(+1)

정리

+- 아닌 -는 야근
+- 아닌 +는 야근
"""
N = int(input())
entryDict = {}
count = 0

for _ in range(N):
    s, p = input().split()
    if s not in entryDict:
        entryDict[s] = p
    else:
        entryDict[s] += p
        
for p in entryDict.values():
    while "+-" in p:
        p = p.replace("+-", "")
    count += len(p)

print(count)