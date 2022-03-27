#BOJ 1181 S5 sort_word

N = int(input())
wordList = list(set([input() for _ in range(N)]))
freqDict = {}

for i in wordList:
    if len(i) not in freqDict:
        freqDict[len(i)] = [i]
    else:
        freqDict[len(i)].append(i)

for freq in sorted(freqDict.keys()):
    for word in sorted(freqDict[freq]):
        print(word)
        
        