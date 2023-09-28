import sys
sys.stdin = open('in5.txt', 'r')
a = [list(map(int, input().split())) for _ in range(9)]
n = len(a)

dict = {}

for i in range(1, 10):
    dict[i] = 0

toggle = True

for i in range(9):
    for j in range(9):
        row_key = a[i][j]
        col_key = a[j][i]
        dict[row_key] += 1
        dict[col_key] += 1

    for key in dict:
        if dict[key] > 2:
            toggle = False
        dict[key] = 0

row_n = 0
col_m = 3

for ket in dict:
    dict[ket] = 0

s = 0
e = 0

while s < 9 and e < 9:
    for i in range(s, s + 3):
        for j in range(e, e + 3):
            dict[a[i][j]] += 1
    e += 3
    for key in dict:
        if dict[key] == 0:
            toggle = False
    if e == 9:
        s += 3
        e = 0

# print(dict)

print(toggle)