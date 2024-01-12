n = int(input())
score = []
summ = 0

for _ in range(n):
    score.append(list(map(int, input().split())))

visited = [False for _ in range(n)]

minn = float('inf')

def combination(pick, level, visited):
    global minn
    if pick == n // 2:
        a_list = []
        b_list = []
        total_a = 0
        total_b = 0
        for i in range(len(visited)):
            if visited[i]:
                a_list.append(i)
            else:
                b_list.append(i)

        for i in a_list:
            for j in a_list:
                if i == j:
                    continue
                else:
                    total_a += score[i][j]

        for i in b_list:
            for j in b_list:
                if i == j:
                    continue
                else:
                    total_b += score[i][j]

        if minn > abs(total_b - total_a):
            minn = abs(total_b - total_a)
        return

    for i in range(level, len(visited)):
        if not visited[i]:
            visited[i] = True
            combination(pick + 1, i + 1, visited)
            visited[i] = False

combination(0, 0, visited)
print(minn)