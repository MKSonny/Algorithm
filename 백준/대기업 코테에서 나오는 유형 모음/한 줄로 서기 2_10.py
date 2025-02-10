import sys
from itertools import permutations

n = int(sys.stdin.readline())
lo = list(map(int, sys.stdin.readline().split()))

# 1 2 3 4
# 2
# (2, 3, 4) => 여기서 2개 고름
# 1
# (3, 4) => 여기서 1개 고름
# 1
# (4) => 여기서 1개 고름
# 0

calc = []
# print(lo)
to = [i for i in range(1, n + 1)]
to_2 = [j for j in range(n, 0, -1)]

te = []

p = permutations(to, n)
p2 = permutations(to_2, n)
t = (p, p2)

def check(li):
    te = [0 for _ in range(len(li))]
    print(li)
    for i in range(len(li)):
        cnt = 0
        for j in range(i, -1, -1):
            if li[j] > li[i]:
                cnt += 1
        te[li[i] - 1] = cnt
    print(te)
    if te == lo:
        for i in li:
            print(i, end=' ')
        exit()
    print()




def check2(li):
    te = [0 for _ in range(n)]
    print(li)
    co = []
    while li:
        a = li.pop()
        co.append(a)
        cnt = 0
        for i in li:
            if i > a:
                cnt += 1
        te[a - 1] = cnt
    # if te == lo:
    #     co.reverse()
    #     for i in co: print(i, end=' ')
    #     # print(co)
    #     # print(te)
    #     exit()
    print(te)
    print()

def check3(li):
    te = [0 for _ in range(n)]
    for idx, i in enumerate(li):
        if i > idx + 1: te[idx] += 1
        # if i > 1: te[i - 1] += 1
        # if i > 2: te[i - 1] += 1
    print(li)
    print(te)
    print()


plo = []
for i in p:
    check3(list(i))