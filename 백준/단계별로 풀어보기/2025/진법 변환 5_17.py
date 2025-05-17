import sys

a, b = sys.stdin.readline().rstrip().split()

s = []

a = list(a)

di = {}
t = 10

for i in range(65, ord('Z') + 1):
    di[chr(i)] = t
    t += 1

for i in range(0, 10):
    di[str(i)] = i

# print(di)

answer = 0

for idx in range(len(a) - 1, -1, -1):
    answer += (int(b) ** (len(a) - idx - 1)) * di[a[idx]]

print(answer)