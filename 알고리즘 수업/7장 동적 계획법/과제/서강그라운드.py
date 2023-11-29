import copy

n, max_range, pathes = map(int, input().split())
item_lists = list(map(int, input().split()))

INF = 9999

board = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    board[i][i] = 0

for i in range(pathes):
    a, b, c = map(int, input().split())
    board[a - 1][b - 1] = c
    board[b - 1][a - 1] = c


def shortest_path_floyd(W, max_range, item_lists):
    vsize = len(W)
    # D0: 아무런 정즘을 거치지 않는 경로

    D = copy.deepcopy(W)

    # 이렇게 반복하면 A가 경유지가 되는 것 같다.
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                # D[i][k] + D[k][j]: i에서 j로 갈 때 k를 거쳐서 가는 경우
                # D[i][j]: i에서 j로 바로 가는 경우
                # print(D[i][k], D[k][j], D[i][j])
                # 첫 반복은 A를 경유지로 설정하고, i는 고정 j는 증가하면..
                # A -> A + A -> (A ~ G) < A -> (A ~ G)
                # i = 1
                # B -> A + A -> (A ~ G) < B -> (A ~ G)
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    # for i in D:
    #     print(i)

    return get_items(D, vsize, max_range, item_lists)

def get_items(board, n, max_range, item_lists):
    total = []
    sub_total = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] <= max_range:
                sub_total += item_lists[j]
        total.append(sub_total)
        sub_total = 0

    return max(total)

print(shortest_path_floyd(board, max_range, item_lists))