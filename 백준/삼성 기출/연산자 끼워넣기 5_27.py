import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
calc = list(map(int, sys.stdin.readline().split()))

maxx = -1
minn = float("inf")

def dfs(level, total, calc):
    global maxx, minn

    if level == len(l):
        # print(total)
        maxx = max(maxx, total)
        minn = min(minn, total)
        return


    for i in range(4):
        if calc[i] > 0:
            calc[i] -= 1
            if i == 0:
                total += l[level]
                dfs(level + 1, total, calc)
                total -= l[level]
            elif i == 1:
                total -= l[level]
                dfs(level + 1, total, calc)
                total += l[level]
            elif i == 2:
                total *= l[level]
                dfs(level + 1, total, calc)
                total //= l[level]
            elif i == 3:
                total //= l[level]
                dfs(level + 1, total, calc)
                total *= l[level]
            calc[i] += 1


visited = [False for _ in range(4)]

dfs(1, l[0], calc)

print(maxx)
print(minn)