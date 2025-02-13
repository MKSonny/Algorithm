import sys

n = int(sys.stdin.readline())
lo = list(map(int, sys.stdin.readline().split()))

te = [0 for _ in range(n)]


for no, i in enumerate(lo):
    cnt = 0
    for idx, ze in enumerate(te):
        if cnt == i and ze == 0:
            te[idx] = no + 1
            break
        elif ze == 0: cnt += 1

print(*te)
