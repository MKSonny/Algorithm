import copy
import sys
from itertools import combinations
from itertools import permutations

n, m, h = map(int, sys.stdin.readline().split())

l = [[] for _ in range(h + 1)]
for_combi = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append((b, b + 1))

cnt = 0

for i in range(1, h + 1):
    visited = [False] * (n + 1)
    for a, b in l[i]:
        visited[a] = True
        if a - 1 >= 0:
            visited[a - 1] = True
        if a + 1 < n:
            visited[a + 1] = True
    for j in range(1, n):
        if not visited[j]:
            for_combi.append((i, j))
            # for_combi.append(str(i) + '|' + str(j))
            cnt += 1

# print('for_combi', cnt)
# for i in for_combi:
#     print(i)
# print()



def test_ladder(for_test_l):
    cnt = 0
    # for i in for_test_l:
    #     print(i)
    # print()
    for start in range(1, n + 1):
        f_p = start
        # print(start, end = ' ')
        level = 1
        while level != h + 1:
            flag = False
            for a, b in for_test_l[level]:
                if a == start:
                    level += 1
                    start = b
                    flag = True
                    break
                if b == start:
                    level += 1
                    start = a
                    flag = True
                    break
            if flag:
                continue
            level += 1
        # print('test')
        # print(f_p, start)
        if f_p == start:
            cnt += 1
    # print(cnt)
    if cnt == n:
        return True


for i in range(1, 3 + 1):
    for a in combinations(for_combi, i):
        temp_l = copy.deepcopy(l)

        for temp_a, temp_b in a:
            # temp_a, temp_b = map(int, t.split('|'))
            # print(temp_a, temp_b)
            temp_l[temp_a].append((temp_b, temp_b + 1))

        # print('temp')
        # for i in temp_l:
        #     print(i)
        if test_ladder(temp_l):
            print(i)
            exit()

print(-1)