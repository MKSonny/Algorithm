def coef_mem(n, k, mem):
    if mem[n][k] == None:
        if k == 0 or k == n:
            mem[n][k] = 1
        else:
            mem[n][k] = coef_mem(n - 1, k - 1, mem) + coef_mem(n - 1, k, mem)

    return mem[n][k]

n, k = map(int, input().split())
mem = [[None for _ in range(k + 1)] for _ in range(n + 1)]
print(coef_mem(n, k, mem))
for i in mem:
    print(i)