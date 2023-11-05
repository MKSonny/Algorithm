def fib_dp_mem(n):
    if mem[n] == None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n - 1) + fib_dp_mem(n - 2)
    return mem[n]

n = 7
mem = [None] * (n + 1)
print(fib_dp_mem(n))

# 둘의 차이는?

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)