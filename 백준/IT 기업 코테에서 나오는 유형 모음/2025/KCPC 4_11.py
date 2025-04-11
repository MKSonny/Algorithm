import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, k, t, m  = map(int, sys.stdin.readline().split())
    l = [{} for _ in range(n)]

    time = [0 for _ in range(n)]

    for x in range(m):
        # 팀 id, 문제 번호, 획득한 점수
        i, j, s = map(int, sys.stdin.readline().split())
        if j not in l[i - 1].keys():
            l[i - 1][j] = s
        else:
            l[i - 1][j] = max(l[i - 1][j], s)
        time[i - 1] = x

    scores = []
    for idx, i in enumerate(l):
        scores.append((sum(i.values()) - len(i) - time[idx], idx + 1))

    scores.sort(reverse=True)
    # print(scores)

    for i in range(len(scores)):
        a, b = scores[i]
        if b == t:
            print(i + 1)
            break

    # print(scores)
    # print(l)

