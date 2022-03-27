#BOj 1157

string = input().lower()
freq = dict()

for i in string:
    if i not in freq:
        freq[i] = 0
        freq[i] += 1
    else:
        freq[i] += 1

freqValue = list(freq.values())
freqKeys = list(freq.keys())

N = freqValue.index(max(freqValue))

if freqValue.count(freqValue[N]) > 1:
    print("?")
else:
    print(freqKeys[N].upper())
