#BOJ 1316 s5 group word checker

"""
중복되는 문자는 뭉탱이로 존재해야 한다...!
문자들의 인덱스 값에 대한 리스트를 생성하고 이를 값으로 대응시킨다.
만약 해당 인덱스 값이 연속적이지 않다면 그룹 단어가 아닌 것으로 판정하자.
"""

wordList = [input() for _ in range(int(input()))]
groupCount = 0

for word in wordList:
    letterDict = {}
    check = 0
    for i in word:
        if i not in letterDict:
            letterDict[i] = []
            index = word.find(i)
            letterDict[i].append(index)
        else:
            index = word.find(i, index + 1)
            letterDict[i].append(index)
    for indexList in letterDict.values():
        if len(indexList) > 1:
            for i in range(len(indexList) - 1):
                if not (indexList[i+1] - indexList[i] == 1):
                    check += 1
    if check == 0:
        groupCount += 1
  
print(groupCount)