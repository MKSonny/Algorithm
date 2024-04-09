import sys

n, m = map(int, sys.stdin.readline().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            home.append((i, j))
        elif l[i][j] == 2:
            chicken.append((i, j))

true_answer = 9999

def calculate(sol):
    global true_answer
    answer = 0

    for home_y_x in home:
        home_y, home_x = home_y_x[0], home_y_x[1]
        min_dis = 9999
        for sol_y_x in sol:
            chicken_y, chicken_x = sol_y_x[0], sol_y_x[1]
            distance = abs(home_y - chicken_y) + abs(home_x - chicken_x)
            min_dis = min(distance, min_dis)
        answer += min_dis

    true_answer = min(answer, true_answer)

def combination(chicken_loc, sol, k, level):
    if len(sol) == k:
        calculate(sol)
        return
    for i in range(level, len(chicken_loc)):
        sol.append(chicken_loc[i])
        combination(chicken_loc, sol, k, i + 1)
        sol.pop()

combination(chicken, [], m, 0)
print(true_answer)