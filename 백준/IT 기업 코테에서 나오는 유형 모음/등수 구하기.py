import sys

n, new_score, p = map(int, sys.stdin.readline().split())

if n > 0:
    l = list(map(int, sys.stdin.readline().split()))
    # if len(l) < p:
    #     p = len(l)
    if p == len(l) and new_score <= l[-1]:
        print(-1)
    else:
        l.append(new_score)
        l.sort(reverse=True)
        rank = l.index(new_score) + 1
        print(rank)
else:
    print(1)