n = int(input())
l = list(map(int, input().split()))
m = int(input())

'''
3
1 2 5
15
'''
l.sort(reverse=True)
a = [0] * n
min_cnt = float('inf')

def dfs(l, level, sol):
    global min_cnt
    if min_cnt < len(sol):
        return
    if sum(sol) > m:
        return
    if sum(sol) == m:
        # print(sol)
        min_cnt = min(min_cnt, len(sol))
        return
    for i in range(n):
        sol.append(l[i])
        dfs(l, level + 1, sol)
        sol.pop()


dfs(l, 0, [])
print(min_cnt)