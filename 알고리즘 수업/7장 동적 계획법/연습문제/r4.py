def coef_mem(n, k, mem):
    if mem[n][k] == None:
        if n == k or k == 0:
            mem[n][k] = 1
        else:
            mem[n][k] = coef_mem(n - 1, k - 1, mem) + coef_mem(n - 1, k, mem)

    return mem[n][k]

def do_coef_mem(n, k):
    mem = [[None for _ in range(k + 1)] for _ in range(n + 1)]
    return coef_mem(n, k, mem)

print(do_coef_mem(4, 2))