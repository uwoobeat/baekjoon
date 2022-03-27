#BOJ 4673 self_number

'''
1. 재귀함수 n을 정의한다.
2. 1 3 5 7 9로 시작하는 d(n) 리스트를 만든다.
'''

def d(n):
    digitSum = sum(map(int, list(str(n))))
    return n + digitSum

def dlist(n, dList = []):
    if 10 <= n <= 10000:
        dList.append(n)
        dList(d(n))
    else:
        return dList

numSet = set(range(1,10000))

for i in [1,3,5,7,9]:
    numSet - set(dlist(i))

print(*numSet)