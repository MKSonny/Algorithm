import sys


n, m = map(int, sys.stdin.readline().split())
l = []
scores = []
rank = {}

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    score = b * 100 + c * 50 + d * 30

    if score not in rank.keys():
        rank[score] = [a]
        scores.append(score)
    else:
        rank[score].append(a)
    l.append((a, score))

print(scores)
l.sort(key=lambda o:o[1], reverse=True)

for i in range(1, n + 1):
    if i == 3:
        

print(rank)