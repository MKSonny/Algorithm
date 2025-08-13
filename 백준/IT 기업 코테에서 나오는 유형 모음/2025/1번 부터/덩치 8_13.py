import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))

scores = []

for i in range(n):
    score = 1
    for j in range(n):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            score += 1
    scores.append(score)

rank = 1

calc = sorted(scores)

dic = dict()

while calc:
    s = calc.pop()
    if s not in dic.keys():
        dic[s] = rank
        rank += 1
    else:
        rank += 1

for i in scores:
    print(i, end=' ')