list = [2, 4, 5, 8, 12]
n = len(list)
select = 3
res = [0] * select
cnt = 0

def dfs(l, s, total):
    global cnt
    if l == select:
        print(total)
    else:
        for i in range(s, n):
            res[l] = list[i]
            dfs(l + 1, i + 1, list[i] + total)

# def dfs(l, s):
#     global cnt
#     if l == select:
#         total = 0
#         for item in res:
#             total += item
#         if total % 6 == 0:
#             cnt += 1
#     else:
#         for i in range(s, n):
#             res[l] = list[i]
#             dfs(l + 1, i + 1)

dfs(0, 0, 0)
# print(cnt)