import sys


n = sys.stdin.readline().rstrip()
l = list(n)

n = len(l)
# print(n)

prev = 0
idx = 1
cnt = -1
is_same = -1

while idx < n:
    # if l[idx] < l[prev]:
    #     cnt += 10
    # list(str(cnt))[0]
    if l[idx] in set(list(str(cnt))) or l[idx] > l[prev]:
        print(l[idx], cnt, set(list(str(cnt))))
        is_same += 1
    else:
        if cnt == -1:
            cnt = 0
        cnt += 10
        # cnt += int(l[idx])
        is_same = -1
    prev = idx
    idx += 1


if list(str(cnt))[0] == l[prev]:
    # print(cnt)
    if is_same > 0:
        print(cnt + is_same)
    else:
        print('work 1', cnt)
else:
    if cnt == -1:
        cnt = 0
    print('work 2', cnt + int(l[prev]))