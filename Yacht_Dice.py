import sys

input = lambda: sys.stdin.readline().rstrip()
pair = lambda : map(int, input().split())

s = input()
nums = list(pair())
snums = set(nums)
score = [0] * 12

max_score = -1

for i in range(12):
    if s[i] == 'Y':
        if 0 <= i <= 5:
            score[i] = (nums.count(i+1) + 2) * (i+1)
        elif i == 6:
            if len(snums) == 1:
                score[i] = nums[0] * 4
            elif len(snums) == 2:
                for j in list(snums):
                    if nums.count(j) == 2:
                        score[i] = j * 4
        elif i == 7:
            if len(snums) == 1:
                tmp = nums[0]
                if tmp == 6:
                    score[i] = tmp * 3 + 5 * 2
                else:
                    score[i] = tmp * 3 + 6 * 2
            elif len(snums) == 2:
                score[i] = max(snums) * 3 + min(snums) * 2
        elif i == 8:
            if len(snums) == 3:
                if 6 not in nums:
                    score[i] = 30
        elif i == 9:
            if len(snums) == 3:
                if 1 not in nums:
                    score[i] = 30
        elif i == 10:
            if len(snums) == 1:
                score[i] = 50
        elif i == 11:
            score[i] = sum(nums) + 12

print(score)