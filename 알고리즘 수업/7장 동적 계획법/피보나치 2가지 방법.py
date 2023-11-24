def table_fib(n):
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 2] + table[i - 1]

    return table[n]

def do_table_mem(n):
    mem = [None] * (n + 1)
    return table_mem(n, mem)

def table_mem(n, mem):
    if mem[n] == None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = table_mem(n - 2, mem) + table_mem(n - 1, mem)
    return mem[n]

print(do_table_mem(7))