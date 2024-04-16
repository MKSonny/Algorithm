import sys

n, m = sys.stdin.readline().split()
n = int(n)
l = []

# Y, F, O
# 2, 3, 4

played = set()

if m == 'Y':
    a = 1
elif m == 'F':
    a = 2
else:
    a = 3

cnt = 0

for _ in range(n):
    player = sys.stdin.readline().rstrip()

    if player not in played:
        played.add(player)
        cnt += 1

print(cnt // a)