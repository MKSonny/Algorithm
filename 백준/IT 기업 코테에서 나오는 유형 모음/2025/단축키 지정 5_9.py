import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(list(sys.stdin.readline().split()))

for i in l:
    for idx, j in enumerate(i):
        i[idx] = list(j)

t_idx = 0
idx = 0

temp = []

for i in l:
    flag = False
    for_print = []

    for j in range(len(i)):
        if flag: continue

        if str.upper(i[j][0]) not in temp:
            temp.append(str.upper(i[j][0]))
            for p in for_print:
                print(''.join(p), end=' ')
            # print(''.join(for_print[:]))
            print('[' + i[j][0] + ']' + ''.join(i[j][1:]), end=' ')
            flag = True

            for k2 in range(j + 1, len(i)):
                print(''.join(i[k2]), end=' ')
            print()
            break

        for_print.append(i[j])

    for_print = []

    if not flag:
        for j in range(len(i)):
            if flag: break
            for k in range(len(i[j])):
                if str.upper(i[j][k]) not in temp:
                    for p in for_print:
                        print(''.join(p), end=' ')

                    print(''.join(i[j][:k]) + '[' + i[j][k] + ']' + ''.join(i[j][k + 1:]), end=' ')
                    temp.append(str.upper(i[j][k]))
                    flag = True

                    for k2 in range(j + 1, len(i)):
                        print(''.join(i[k2]), end=' ')
                    print()
                    break

            for_print.append(i[j])

    if not flag:
        for j in i:
            print(''.join(j), end=' ')
        print()