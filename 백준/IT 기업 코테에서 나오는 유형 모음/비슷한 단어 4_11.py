import copy
import sys

n = int(sys.stdin.readline())
words = []
di = {}

for i in range(65, 65 + 26):
    di[chr(i)] = 0


for _ in range(n):
    l = list(sys.stdin.readline().rstrip())
    words.append(l)


a = words.pop(0)

a_d = copy.deepcopy(di)
for i in a:
    a_d[i] += 1

answer = 0

for i in words:
    temp = copy.deepcopy(di)
    for j in i:
        temp[j] += 1

    diff = 0

    for k in di.keys():
        diff += abs(temp[k] - a_d[k])

    # print(diff)

    if len(i) == len(a) and diff <= 2:
        answer += 1
    elif diff <= 1:
        answer += 1

# print()
print(answer)