import sys


n = int(sys.stdin.readline())
l = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().rstrip().split())
    l.append((weight, height))

answer = [0] * (n)

for i in range(n - 1):
    cnt = 0
    for j in range(i + 1, n):
        if l[i][0] > l[j][0] and l[i][1] > l[j][1]:
            answer[i] += 1
        elif l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            answer[j] += 1

sorted_data = sorted(answer, reverse=True)

ranks = []

for num in answer:
    rank = sorted_data.index(num) + 1
    ranks.append(rank)

for i in ranks:
    print(i, end=' ')