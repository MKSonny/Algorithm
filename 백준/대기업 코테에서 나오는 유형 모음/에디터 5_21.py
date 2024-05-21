import sys

l = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
order = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    order.append(a)

# print(order)

cursor = len(l)

for i in order:
    if len(i) > 1:
        a, b = i.split()
    else:
        a = i
    if cursor < 0:
        cursor = 0
    if cursor > len(l):
        cursor = n
    if a == 'P':
        l.insert(cursor, b)
        cursor += 1
    elif a == 'L':
        cursor -= 1
    elif a == 'B':
        cursor -= 1
        if cursor < 0:
            continue
        l.pop(cursor)
    elif a == 'D':
        cursor += 1

print(''.join(l))