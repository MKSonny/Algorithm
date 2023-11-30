def bino_coef(n, k, mem):
    if mem[n][k] == None:
        if n == k or k == 0:
            mem[n][k] = 1
        else:
            mem[n][k] = bino_coef(n - 1, k - 1, mem) + bino_coef(n - 1, k, mem)
    return mem[n][k]

def do_bino_coef(n, k):
    mem = [[None for _ in range(k + 1)] for _ in range(n + 1)]

    bino_coef(n, k, mem)
    for i in mem:
        print(i)

print(do_bino_coef(4, 2))
