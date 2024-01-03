n = int(input())
l = []

for i in range(1, n + 1):
    if i == 1:
        l.append(1)
    elif i == 2:
        l.append(2)
    else:
        a = l.pop(0)
        b = l[-1]
        l.append(a + b)

print(l[-1])
