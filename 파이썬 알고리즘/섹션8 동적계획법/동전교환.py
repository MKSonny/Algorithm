n = int(input())
l = list(map(int, input().split()))
m = int(input())

l.sort(reverse=True)

total = 0

print(l)
total = 0

for val in l:
    cnt = (m // val)
    total += cnt
    m -= cnt * val

print(total)