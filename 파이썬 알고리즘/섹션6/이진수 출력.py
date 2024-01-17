n = int(input())
s = []

def dfs(n):
    if n == 0:
        return
    dfs(n // 2)
    print(n % 2, end='')

dfs(n)