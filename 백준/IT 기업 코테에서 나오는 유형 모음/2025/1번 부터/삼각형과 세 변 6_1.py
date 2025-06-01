import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break

    l = [a, b, c]
    l.sort()

    if l[-1] >= l[0] + l[1]:
        print("Invalid")
        continue

    s = set([a, b, c])

    if len(s) == 3:
        print('Scalene')
    elif len(s) == 2:
        print('Isosceles')
    else:
        print('Equilateral')