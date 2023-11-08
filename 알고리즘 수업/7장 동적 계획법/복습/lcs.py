string_a = list("HELLO WORLD")
string_b = list("GAME OVER")

def lcs(a, b):
    mem = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

    for i in range(len(b) + 1):
        for j in range(len(a) + 1):
            if i == 0 or j == 0:
                mem[i][j] = 0
            elif b[i - 1] == a[j - 1]:
                mem[i][j] = mem[i - 1][j - 1] + 1
            else:
                mem[i][j] = max(mem[i - 1][j], mem[i][j - 1])
    return mem

def track(a, b, mem):
    same = ''
    n = len(a) - 1
    m = len(b) - 1
    while n > 0 and m > 0:
        if mem[n][m] > mem[n - 1][m] and mem[n][m] > mem[n][m - 1]:
            same += a[n]
            n -= 1
            m -= 1
        elif mem[n][m] == mem[n][m - 1]:
            m -= 1
        elif mem[n][m] == mem[n - 1][m]:
            n -= 1
        print(same)

mem = lcs(string_a, string_b)
for i in mem:
    print(i)
print(mem[len(string_b)][len(string_a)])
# track(string_a, string_b, mem)