x, w = map(int, input().split())
v = []
for _ in range(x):
    v.append(int(input()))

def dp_answer2(x, W, v):
    mem = [[1 for _ in range(W + 1)] for _ in range(x)]

    for i in range(x):
        for w in range(W + 1):
            



def dp_answer(x, W, v):
    mem = [[0 for _ in range(W + 1)] for _ in range(x)]

    for i in range(1, x + 1):
        for w in range(1, W + 1):
            if v[i - 1] == 1:
                mem[i][w] = 1
            # 가치가 곧 무게, 가치와 무게가 같은, 무한대로 생성가능한 물건
            elif w - v[i - 1] > 0:
                mem[i][w] = mem[i][w - v[i - 1]] + mem[i - 1][w]
            else:
                mem[i][w] = mem[i - 1][w]

    for i in mem:
        print(i)

def dp(x, w, v):
    mem = [[0 for _ in range(w + 1)] for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, w + 1):
            if v[i - 1] == 1:
                mem[i][j] = 1
            elif j // v[i - 1] > 0:
                mem[i][j] = j // v[i - 1] + mem[i - 1][j] + 1
            else:
                mem[i][j] = mem[i - 1][j]
    for i in mem:
        print(i)
    return mem[x][w]

print(dp_answer(x, w, v))