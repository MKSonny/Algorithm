import sys

l = list(sys.stdin.readline().rstrip())
result = []
window_size = l.count('a')

l = l + l
# n = 4, a = 2
minn = float('inf')
for i in range(len(l) - window_size):
    # result.append((i, l[i:i + window_size].count('b')))
    minn = min(minn, l[i:i + window_size].count('b'))

print(minn)