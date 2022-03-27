"""
1. 문자열을 같은 문자 기준으로 나눈다.
2. 나눠진 문자열을 다음 규칙에 따라 치환한다.
    1) 길이가 K 이상이면 1
    2) 길이가 K 미만이면 0
    3) 이미 치환된 적 있으면 삭제

딕셔너리로 다루는 것이 좋을 것 같다.
A : 3, B : 3, C : 1 이런 식으로...
"""

S, K = input().lower().split()
splitDict = {}
countCheck = {}
catString = ""
    
for i in range(len(S)):
    if S[i] not in splitDict:
        splitDict[S[i]] = 1
        countCheck[S[i]] = 0
    else:
        if S[i-1] == S[i]:
            if countCheck[S[i]] == 0:
                splitDict[S[i]] += 1
        else:
            countCheck[S[i]] = 1

print(splitDict)

for i in splitDict:
    if splitDict[i] >= int(K):
        catString += "1"
    else:
        catString += "0"

print(catString)