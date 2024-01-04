l = [
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]

n = len(l)

# for i in range(len(l[0])): # 원래 가로
#     for j in range(n):
#         print(l[j][i], end=' ')
#     print()
# print()
#
# for i in range(n - 1, -1, -1):
#     for j in range(len(l[0]) - 1, -1, -1):
#         print(l[i][j], end=' ')
#     print()
# print()

mem = [[-1] * n for _ in range(len(l[0]))]  # n x m 크기의 2차원 배열 생성
mem2 = [[-1] * n for _ in range(len(l[0]))]  # n x m 크기의 2차원 배열 생성
mem3 = [[-1] * len(l[0]) for _ in range(n)]  # n x m 크기의 2차원 배열 생성

for i in range(n):
    for j in range(len(l[0])):
        # print(l[i][j], end=' ')
        mem[j][i] = l[n - 1 - i][j]
        mem2[j][i] = l[i][j]
        mem3[i][j] = l[n - 1 - i][len(l[0]) - 1 - j]

for i in l:
    print(i)

print()

for j in mem:
    print(j)

print()

for i in mem2:
    print(i)

print()

for i in mem3:
    print(i)