import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m, st = sys.stdin.readline().rstrip().split()
    m = int(m)
    li = list(st)
    for i in li:
        print(i * m, end='')
    print()