fib_0 = [0 for _ in range(40 + 1)]
fib_0[0] = 1
fib_0[1] = 0

fib_1 = [0 for _ in range(40 + 1)]
fib_1[0] = 0
fib_1[1] = 1

# fib_1[0] == fib_0[1]

for i in range(2, 40 + 1):
    fib_0[i] = fib_0[i - 2] + fib_0[i - 1]
    fib_1[i] = fib_1[i - 2] + fib_1[i - 1]

n = int(input())
l = []

for _ in range(n):
    l.append(int(input()))

for v in l:
    print(fib_0[v], fib_1[v])
# print(fib_0)
# print(fib_1)