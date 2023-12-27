import sys

input = sys.stdin.readline

def combination(n, k, sol, level):
    if len(sol) == k:
        print(' '.join(map(str, sol)))
        return

    for i in range(level, len(n)):
        sol.append(n[i])
        combination(n, k, sol, i + 1)
        sol.pop()

while True:
    l = list(map(int, input().split()))
    combination(l[1:], 6, [], 0)
    print()
    if l[0] == 0:
        break