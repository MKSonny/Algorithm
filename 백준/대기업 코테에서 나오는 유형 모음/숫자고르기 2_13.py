import sys
from itertools import combinations

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

to = []

for idx, i in enumerate(li):
    to.append((idx + 1, i))




# ((1, 3), (3, 1), (5, 5))
def check(te):
    di = {}

    for a, b in te:
        if a not in di.keys():
            di[a] = 1
        else:
            di[a] += 1

        if b not in di.keys():
            di[b] = 1
        else:
            di[b] += 1

        if di[a] > 2 or di[b] > 2:
            return False

    for d in di:
        if di[d] < 2:
            return False

    return True


flag = False


for m in range(n - 1, 0, -1):
    c = combinations(to, m)

    for i in c:
        if check(i):
            # print(i)
            flag = True

            an = []
            for k in i:
                an.append(k[0])

            an.sort()

            print(m)
            for a in an:
                print(a)

            break

    if flag: break
    # print(i)