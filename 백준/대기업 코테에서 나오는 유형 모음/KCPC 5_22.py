# 12:38
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k, my_team, m = map(int, sys.stdin.readline().split())
    l = []
    for i in range(n):
        d = {}
        for i in range(1, k + 1):
            d[i] = 0
        d['cnt'] = 0
        d['recent'] = 0
        l.append(d)



    for r in range(m):
        team, num, score = map(int, sys.stdin.readline().split())
        l[team - 1]['cnt'] += 1
        l[team - 1]['recent'] = r
        if l[team - 1][num] < score:
            l[team - 1][num] = score

    # for i in l:
    #     print(i)
    # print()
    total_l = []
    # for i in l:
    #     total_l.append(sum(i.values()))
    for i in l:
        total = 0
        for k in range(1, k + 1):
            total += i[k]
        total_l.append((total, i['cnt'], i['recent']))

    # print(total_l)
    sort_total = sorted(total_l, key=lambda o:(o[0], -o[1], -o[2]), reverse=True)
    rank = []
    # print(sort_total)
    for i in total_l:
        rank.append(sort_total.index(i) + 1)
    # print(rank)

    print(rank[my_team - 1])


# print(l)