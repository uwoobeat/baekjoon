#16916 part_str

"""
kmp 알고리즘은 너무 어렵다...
그냥 in operator 쓰자.

정규 표현식 (regular expression)
- 문자열의 특정 패턴을 나타내는 데 쓰는 표현식
- 특정 문자열을 찾거나 특정 패턴을 찾아서 변환할 때 사용
- ex : 전화번호 패턴인 "xxx-xxxx-xxxx" 찾기, 에러 패턴인 "에러 xxxx" 찾기 등등...
- 파이썬에서는 re module로 정규식 기능 지원

- re.compile로 정규식 패턴을 받아서 정규식 객체 (re.RegexObject 클래스 객체) 반환
- 다양한 메서드가 있음
- re.match의 경우 패턴과 문자열이 동일한지 확인
- re.search의 경우 문자열 안에 해당 패턴이 있는지 확인, 매칭 위치와 패턴 등 정보 포함된 re.Match 객체 반환
- 없다면 None을 반환
- re.Match 객체의 불린값은 참이고 None의 불린값은 거짓...

속도는 당연히 in operator가 더 빠르다.
문자열의 길이가 매우 길다면 두 문자열을 입력받을 때 comprehension을 사용하지 않는 것이 좋다.
입력값을 바로 변수에 할당하는 것과 입력값 둘을 리스트로 묶어서 각각 할당해주는 것 사이에는 속도 차이가 존재하기 때문.
"""

import sys
import re
input = sys.stdin.readline

#sol 1 - timeout
s, p = [input() for _ in range(2)]

if p in s:
    print(1)
else:
    print(0)

#sol 2 - regex

s, p = [input().rstrip() for _ in range(2)]
p = re.compile(p)

if p.search(s):
    print(1)
else:
    print(0)
    
#sol 3 - comprehension

s = input().rstrip()
p = input().rstrip()
print(1) if p in s else print(0) #comprehension