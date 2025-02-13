import sys
from itertools import combinations

n, k, p, x = map(int, sys.stdin.readline().split())

di = {
    '0': [1, 1, 1, 1, 1, 1, 0],
    '1': [0, 1, 1, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1],
    '3': [1, 1, 1, 1, 0, 0, 1],
    '4': [0, 1, 1, 0, 0, 1, 1],
    '5': [1, 0, 1, 1, 0, 1, 1],
    '6': [1, 0, 1, 1, 1, 1, 1],
    '7': [1, 1, 1, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1],
    }

di2 = {
    '[1, 1, 1, 1, 1, 1, 0]': 0,
    '[0, 1, 1, 0, 0, 0, 0]': 1,
    '[1, 1, 0, 1, 1, 0, 1]': 2,
    '[1, 1, 1, 1, 0, 0, 1]': 3,
    '[0, 1, 1, 0, 0, 1, 1]': 4,
    '[1, 0, 1, 1, 0, 1, 1]': 5,
    '[1, 0, 1, 1, 1, 1, 1]': 6,
    '[1, 1, 1, 0, 0, 0, 0]': 7,
    '[1, 1, 1, 1, 1, 1, 1]': 8,
    '[1, 1, 1, 1, 0, 1, 1]': 9,
    }

x = list(str(x))

def toggle(li, ori):
    co = ori[:]
    # print("ori", ori)
    # print('te', di2[str(co)])
    for i in li:
        if co[i] == 1:
            co[i] = 0
        else:
            co[i] = 1

    # print(str(co))

    if str(co) in di2.keys():
        print(di2[str(co)])

ori = ''
for i in x:
    ori += str(di[i])

print(ori)
ch = [i for i in range(1, 8 * k + 1)]

for p in range(1, p + 1):
    c = combinations(ch, p)
    for t in c:
        print(t)
    # for t in c:
    #     toggle(t, ori)