import sys
input = sys.stdin.readline

s = input().rstrip()
openCount = 0
closeCount = 0
curopen = 0 #현재 여 갯수
curclose = 0 #현재 닫 갯수
tmp = s[0] #구간 확인을 위한 변수
sectPos = 0 #구간 시작 위치
sectLen = 0 #구간 길이
res = 0
is_prob_raised = False

def count(letter):
    global openCount, closeCount, curopen, curclose
    if letter == '(':
        openCount += 1
        curopen += 1
    else:
        closeCount += 1
        curclose += 1
        
def section_check(i, letter):
    global tmp, sectPos, sectLen
    if letter != tmp: #이번 문자가 이번 문자와 다르면
        tmp = letter #구간 갱신
        sectPos = i #구간 시작 위치
        sectLen = 1 #구간 길이 초기화
    else:
        sectLen += 1 #같으면 구간 길이 +1

for i in range(len(s)):
    letter = s[i]
    count(letter)
    section_check(i, letter)
    if curopen < curclose:
        print("문제 구간", i, s[i], "시작 (닫는 문자여야 함)")
        res = curclose #len(s[sectPos:sectPos+curopen]) 아닌가?
        curopen, curclose = 0, 0
        is_prob_raised = True
        break

if not is_prob_raised:
    if s[0:1] == "()":
        

print(res)
    
    