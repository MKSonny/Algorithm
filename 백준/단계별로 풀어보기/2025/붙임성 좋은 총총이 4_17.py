import sys

n = int(sys.stdin.readline())

dancing = {'ChongChong'}

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    if a in dancing or b in dancing:
        dancing.add(a)
        dancing.add(b)

print(len(dancing))