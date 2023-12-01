n = int(input())

mem = [None] * (n + 1)

def make_1(mem, m):
    if mem[m] is None:
        if m == 0 or m == 1:
            mem[m] = 0
        else:
            mem[m] = make_1(mem, m - 1) + 1
            if m % 3 == 0:
                mem[m] = min(mem[m], make_1(mem, m // 3) + 1)
            if m % 2 == 0:
                mem[m] = min(mem[m], make_1(mem, m // 2) + 1)

    return mem[m]

print(make_1(mem, n))