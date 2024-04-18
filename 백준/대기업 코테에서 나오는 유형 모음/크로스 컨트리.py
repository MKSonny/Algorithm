import sys

t = int(sys.stdin.readline())

def collect(teams, l, n, e):
    t_score = [[] for _ in range(200 + 1)]
    real = teams - e
    rank = 1

    for i in range(n):
        if l[i] in real:
            t_score[l[i]].append(rank)
            rank += 1

    min_i = -1
    prev = float('inf')
    minn = float('inf')

    for real_team in real:
        total = sum(t_score[real_team][:4])
        # print(real_team, total, t_score[real_team])
        if minn == total:
            if t_score[real_team][4] < prev:
                min_i = real_team
                prev = t_score[real_team][4]
                continue

        if minn > total:
            minn = total
            prev = t_score[real_team][4]
            min_i = real_team


    return min_i



answer = []
for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    teams = set(l)
    e = set()

    for team in teams:
        if l.count(team) != 6:
            e.add(team)


    answer.append(collect(teams, l, n, e))

for i in answer:
    print(i)