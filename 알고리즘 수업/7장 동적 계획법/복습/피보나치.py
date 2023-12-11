def fib(n):
    mem = [None] * (n + 1)

    for i in range(n + 1):
        if i < 2:
            mem[i] = i
        else:
            mem[i] = mem[i - 1] + mem[i - 2]

    return mem[n]

def do_fib(n):
    mem = [None] * (n + 1)
    print(fib_mem(n, mem))

def fib_mem(n, mem):
    if mem[n] == None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_mem(n - 1, mem) + fib_mem(n - 2, mem)

    return mem[n]

# 0 1 1 2 3 5
print(fib(6))
do_fib(6)