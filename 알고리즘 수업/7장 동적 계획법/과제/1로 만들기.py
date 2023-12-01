n = int(input())

mem = [0] * (n + 1)

def make_1(mem, m):
    for i in range(1, m + 1):
        if i - 1 != 0:
            mem[i] = mem[i - 1] + 1
        if i % 3 == 0:
            mem[i] = min(mem[i], mem[i // 3] + 1)
        if i % 2 == 0:
            mem[i] = min(mem[i], mem[i // 2] + 1)
    return mem[m]

print(make_1(mem, n))