import sys

n, m = map(int, sys.stdin.readline().split())
lo = list(map(int, sys.stdin.readline().split()))


board = [[0 for _ in range(m)] for _ in range(n)]

# for i in board:
#     print(i)

for idx, k in enumerate(lo):
    cnt = 0
    to = 0
    for i in range(n):
        if cnt == k: break
        board[i][idx] = 1
        cnt += 1


def check(li):
    st = False
    # print(li)
    total = 0
    for i in range(len(li)):
        if li[i] == 1 and not st:
            st = True
            # print(i)
            cnt = 0
            continue
        if li[i] == 0 and st:
            cnt += 1
            continue
        if li[i] == 1 and st:
            total += cnt
            cnt = 0
            st = True

    return total

an = 0
# for i in board:
#     print(i)
# print()

for i in board:
    an += check(i)

print(an)

# for i in range(n):
#     di = {}
#     for j in range(m):
#         if board[i][j] == 1:
#