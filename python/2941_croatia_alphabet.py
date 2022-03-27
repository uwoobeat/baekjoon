#BOJ 2941 S5 croatia alphabet

"""
<풀이 설계>

특정 문자열은 문자 하나로 인식된다. 이 문자열은 총 8가지가 존재한다.
다만 replace를 사용하게 되면 ddz=dz=의 경우 dz=를 제거하여 dze=가 남으므로 문제가 발생한다.
따라서 변환된 알파벳을 알파벳이 아닌 무언가로 표현해주어야 한다...! 여기서는 인식 문자열 리스트의 인덱스로 하였다.
"""

alphaList = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="] #"dz=" must be searched first

string = input()

for i in alphaList:
    while True:
        if i in string:
            string = string.replace(i, str(alphaList.index(i))) #croatian alphabet is replaced by index of alphaList
        else:
            break

print(len(string))