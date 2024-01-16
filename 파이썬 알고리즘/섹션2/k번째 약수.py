n, m = map(int, input().split())

h = [1]

for i in range(2, n):
    if n % i == 0:
        h.append(i)

h.append(n)

print(h[m - 1])