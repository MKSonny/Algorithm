import sys

s = sys.stdin.readline().rstrip()


l = [0 for _ in range(ord('z') - ord('a') + 1)]

for i in s:
    l[ord(i) - 97] += 1

for i in range(len(l)):
    l[i] = str(l[i])

print(' '.join(l))