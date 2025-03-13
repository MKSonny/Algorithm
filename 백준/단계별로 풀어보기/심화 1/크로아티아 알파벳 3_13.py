import sys

word = list(sys.stdin.readline().rstrip())
idx1 = 0
idx2 = 0

d = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
temp = []

for i in range(len(word) - 2 + 1):
    print('i', i)
    if ''.join(word[i:i + 2]) in d:
       cnt += 1
       i += 1

print(cnt)