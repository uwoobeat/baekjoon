def solution(s, skip, index):
    skipIndexArr = []
    answer = ''
    
    for i in skip:
        skipIndexArr.append(ord(i) - ord('a'))

    for i in s:
        order = ord(i) - ord('a')
        cnt = index
        curIdx = order
        while cnt:
            if curIdx >= 25:
                curIdx -= 25
            else:
                curIdx += 1
            if curIdx not in skipIndexArr:
                cnt -= 1
        answer += chr(curIdx + ord('a'))

    return answer