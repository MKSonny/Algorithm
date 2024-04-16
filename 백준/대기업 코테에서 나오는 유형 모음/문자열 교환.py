import sys

l = list(sys.stdin.readline().rstrip())

idx = 1
prev = 0
cur = -1
answer = 0

while idx < len(l):
    if l[idx] == 'b':
        if l[prev] != l[idx] and cur != -1:
            # print(cur, idx)
            l[cur + 1], l[idx] = l[idx], l[cur + 1]
            cur += 1
            answer += 1
        # l[cur + 1], l[idx] = l[idx], l[cur + 1]
        if l[idx] == l[prev] and l[idx] == 'b':
            cur = idx
    idx += 1
    prev += 1

print(l.sort())
print(l)
# print(answer)