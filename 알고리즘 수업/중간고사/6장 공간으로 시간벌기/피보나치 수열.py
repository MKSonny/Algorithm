mem = [0] * 100
def fib(n):
    for i in range(0, n + 1):
        if i == 0:
            mem[i] = 0
        elif i == 1:
            mem[i] = 1
        else:
            mem[i] = mem[i - 1] + mem[i - 2]
    print(mem[i])

fib(10)