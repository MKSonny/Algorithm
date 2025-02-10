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

te = []

p = permutations(to, n)

def check(li):
    te = [0 for _ in range(len(li))]
    # print(li)
    for i in range(len(li)):
        cnt = 0
        for j in range(i, -1, -1):
            if li[j] > li[i]:
                cnt += 1
        te[li[i] - 1] = cnt
    # print(te)
    if te == lo:
        for i in li:
            print(i, end=' ')
        exit()
    # print()


for i in p:
    # print(i)
    check(i)