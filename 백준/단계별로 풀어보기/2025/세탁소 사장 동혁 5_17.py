import sys

n = int(sys.stdin.readline())

for _ in range(n):
    answer = []

    t = int(sys.stdin.readline())
    answer.append(t // 25)
    t %= 25
    answer.append(t // 10)
    t %= 10
    answer.append(t // 5)
    t %= 5
    answer.append(t // 1)

    for i in answer:
        print(i, end=' ')
    print()