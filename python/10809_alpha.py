#BOJ 10809

"""
1. a~z를 키로, 키 카운트 디폴트값인 -1을 값으로 가지는 딕셔너리를 만든다.
2. 문자열을 입력받는다.
3. 알파벳 리스트의 요소들에 대하여 다음을 반복한다: 만약 문자열에 요소 i가 있다면, i를 키로 가지는 딕셔너리의 값에 i의 인덱스를 할당한다. 
"""

from string import ascii_lowercase

asciiDict = dict(zip(list(ascii_lowercase), [-1] * 26))
string = input()

for i in asciiDict.keys():
    if i in string:
        asciiDict[i] = string.index(i)

print(*asciiDict.values())
        
    