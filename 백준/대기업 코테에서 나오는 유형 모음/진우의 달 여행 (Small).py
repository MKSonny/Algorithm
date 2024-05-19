import sys

n, m = map(int, sys.stdin.readline().split())

l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

minn = float('inf')
move = [-1, 0, 1]
def dfs(l, level, prev, total, moving):
    global minn
    if level == n:
        minn = min(total, minn)
        return
    for i in range(3):
        if i != moving:
            m_l = prev + move[i]
            if m_l < 0:
                m_l = 0
                moving = 0
            if m_l >= m:
                m_l = m - 1
                moving = 0
            total += l[level][m_l]
            print(l[level][m_l], i, moving)
            dfs(l, level + 1, m_l, total, i)
            print()
            total -= l[level][m_l]

dfs(l, 0, 0, 0, -1)

print(minn)