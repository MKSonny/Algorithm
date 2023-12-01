n, m = map(int, input().split())

who_knows = list(map(int, input().split()))
who_knows = set(who_knows[1:])

parties = []

for i in range(m):
    names = list(map(int, input().split()))
    parties.append(set(names[1:]))

for _ in range(m):
    for party in parties:
        if party & who_knows:
            # 어떤 파티에 진실을 알고 있는 사람과
            # 진실을 몰랐던 사람이 있다면
            # 진실을 몰랐던 사람은 진실을 알게 되는 것과 같은 것
            who_knows = who_knows.union(party)

cnt = 0

for party in parties:
    if party & who_knows:
        continue
    cnt += 1

print(cnt)