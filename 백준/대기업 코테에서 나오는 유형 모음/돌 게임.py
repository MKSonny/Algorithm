import sys

n = int(sys.stdin.readline().rstrip())

l = ['SK', 'CY']

toggle = 0

if n == 1:
    print('SK')

while n > 0:
    if n > 3:
        n -= 3
    else:
        n -= 1
    toggle += 1
    if n == 1:
        # win
        print(l[toggle % 2])
        break