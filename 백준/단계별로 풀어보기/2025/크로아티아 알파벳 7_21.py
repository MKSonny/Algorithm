s = input()
di = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}

# for i in range(len(s) - 2 + 1):
i = 0
cnt = 0

# f1, f2 = False, False

while i <= len(s) - 2 + 1:
    f1, f2 = False, False

    if s[i:i + 3] in di:
        i += 3
        f1 = True
    if s[i:i + 2] in di and not f1:
        f2 = True
        i += 2
    if not f1 and not f2:
        i += 1

    cnt += 1

print(cnt)

# for i in range(len(s) - 3 + 1):
#     if s[i:i + 3] in di:
#         print('true', s[i:i + 3])

