#BOJ 18129 B1 strange_code

"""
1.temp에 연속된 문자열을 하나씩 저장하고, 이를 splitList에 추가한다.
2.연속된 문자열이 무엇으로 이루어져 있는지 확인하는 countDict를 생성한다.
3.countDict에 존재하지 않는 경우에만(즉 처음 변환되는 경우에만) 분할된 문자열을 변환해준다.

문자를 분할하는 과정(splitList 생성)이 조금 투박하다.
알파벳은 아스키 코드로 다룰 수도 있었다. (chd(), ord()도 이젠 써도 된다.)
아직도 컴공개 과제에서 헤어나오지 못하는 코드들...
이 문제도 그렇고 다른 문제도 그렇고 체크값을 정갈하게? 만드는 논리가 중요해보인다.
"""

S, K = input().lower().split()

splitList = []
countDict = {}
catString = ""
temp = ""

for i in range(len(S)):
    if i > 0:
        if S[i] == S[i-1]:
            temp += S[i]
        else:
            splitList.append(temp)
            temp = ""
            temp += S[i]
    else:
        temp += S[i]

splitList.append(temp)

for i in splitList:
    if i[0] not in countDict:
        countDict[i[0]] = 1
        if len(i) >= int(K):
            catString += "1"
        else:
            catString += "0"

print(catString)