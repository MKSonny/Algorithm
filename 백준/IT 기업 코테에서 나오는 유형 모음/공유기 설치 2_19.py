import sys

n, c = map(int, sys.stdin.readline().split())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()

start = 0
end = li[-1] - li[0]

while start <= end:
    mid = (start + end) // 2
    current = li[0]
    count = 1

    for i in range(1, n):
        if li[i] >= current + mid:
            count += 1
            current = li[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)