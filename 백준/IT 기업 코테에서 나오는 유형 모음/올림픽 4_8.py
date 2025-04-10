import sys

n, m = map(int, sys.stdin.readline().split())
score = []

for _ in range(n):
    num, gold, silver, bronze = map(int, sys.stdin.readline().split())
    s = gold * 3 + silver * 2 + bronze * 1
    if s in score:
        continue
    score.append(s)

for _ in range(n):
    num, gold, silver, bronze = map(int, sys.stdin.readline().split())
    s = gold * 3 + silver * 2 + bronze * 1
    

print(score)