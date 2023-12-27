n = 642

for j in str(n):
    if j == str(n)[0]:
        continue

    d -= int(j)
    prev_d = d
    print(prev_d, d)
    if prev_d == d:
        continue
    else:
        print('b')
        break
    # print(int(j))