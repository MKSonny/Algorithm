import sys

li = list(sys.stdin.readline().rstrip())
di = {'1': 0, '0': 0}

for i in li:
    di[i] += 1

st = 0
ed = len(li) - 1

num = ['0', '1']

zero_max = di['0'] // 2
one_max = di['1'] // 2

zero_cnt = 0
one_cnt = 0

zero_flag = False

if zero_max == 0:
    zero_flag = True

one_flag = False

if one_max == 0:
    one_flag = True

while not zero_flag or not one_flag:
    if li[st] == '1' and not one_flag:
        li[st] = 'x'
        one_cnt += 1
        if one_cnt == one_max: one_flag = True

    if li[ed] == '0' and not zero_flag:
        li[ed] = 'x'
        zero_cnt += 1
        if zero_cnt == zero_max: zero_flag = True

    st += 1
    ed -= 1


for i in li:
    if i == 'x': continue
    print(i, end='')