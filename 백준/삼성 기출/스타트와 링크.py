'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
n = int(input())
score = []
summ = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    score.append(tmp)
    summ += sum(tmp)

h = []

pos = [i for i in range(0, n)]

minn = float('inf')

def combination(l, level, sol, k, score):
    global minn
    if len(sol) == k:
        if k > 2:
            combination(sol, 0, [], 2, score)
        if k == 2:
            # remaining = list(set(l) - set(sol))
            # print(sol, remaining)
            # first = score[remaining[0]][remaining[1]] + score[remaining[1]][remaining[0]]
            print(sol)
            # second = score[sol[0]][sol[1]] + score[sol[1]][sol[0]]
            # d = abs(first - second)
            # if d < minn:
            #     minn = d
        return

    for i in range(level, len(l)):
        sol.append(l[i])
        combination(l, i + 1, sol, k, score)
        sol.pop()

combination(pos, 0, [], 3, score)
print(minn)