def coef(n, k, mem):
    if mem[n][k] == None:
        if k == 0 or k == n:
            mem[n][k] = 1
        else:
            mem[n][k] = coef(n - 1, k - 1, mem) + coef(n - 1, k, mem)

    return mem[n][k]

def do_coef(n, k):
    mem = [[None for _ in range(k + 1)] for _ in range(n + 1)]

    print(coef(n, k, mem))
    for i in mem:
        print(i)

do_coef(5, 2)