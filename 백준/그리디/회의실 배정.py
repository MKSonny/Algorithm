import sys

input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    a, b = map(int, input().split())
    h.append((a, b))

h.sort(key=lambda o:o[1])

cnt = 0
end_time = 0

for start, end in h:
    if end_time <= start:
        cnt += 1
        end_time = end

print(cnt)
