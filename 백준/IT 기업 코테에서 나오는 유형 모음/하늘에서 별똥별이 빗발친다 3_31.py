import sys

n, m, l, k = map(int, sys.stdin.readline().split())

stars = []
row_l = []
col_l = []

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    stars.append((a, b))
    row_l.append(a)
    col_l.append(b)

row_l.sort()
col_l.sort()

# print(row_l)
# print(col_l)

w_row_l = []
w_col_l = []

def check(idx, li):
    cnt = 0
    q = [li[idx]]
    idx += 1

    while idx < k:
        cnt += li[idx] - q[-1]
        if cnt > l: break
        q.append(li[idx])
        idx += 1

    return q


for i in range(k - 1):
    # print(check(i, row_l))
    w_row_l.append(check(i, row_l))
    w_col_l.append(check(i, col_l))


# print(w_row_l)
# print(w_col_l)
#
answer = []

for i in w_row_l:
    for j in w_col_l:
        min_row, max_row = i[0], i[-1]
        min_col, max_col = j[0], j[-1]
        temp_k = k
        for star_row, star_col in stars:
            if min_row <= star_row <= max_row and min_col <= star_col <= max_col:
                temp_k -= 1
        answer.append(temp_k)

if len(answer) == 0:
    print(k - 1)
else:
    print(min(answer))