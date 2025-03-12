import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
ground = [[5 for _ in range(n)] for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]
s2d2 = []
# dead_trees = {}

for _ in range(n):
    s2d2.append(list(map(int, sys.stdin.readline().split())))


# def make_key(y, x):
#     return str(y) + '_' + str(x)


for _ in range(m):
    y, x, age = map(int, sys.stdin.readline().split())
    # y -= 1
    # x -= 1
    trees[y - 1][x - 1].append(age)
    # key = make_key(y, x)
    # if key in trees:
    #     trees[key].append(age)
    # else:
    #     trees[key] = [age]

'''
가장 처음에 양분은 모든 칸에 5만큼 들어있다.
같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
(봄) 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
y, x = [1, 2, 3]
만약 3이 죽는다면 -> 그냥 3을 제거 pop, remove, 인덱스는 구분 안해도 될 것 같다.
근데 리스트 내부의 값을 수정할 수 있나
while문으로 해결 -> deque() -> pop하고 다시 insert하면 무한루프
-> 인덱스 위치를 기억해야 할 듯

봄: 나이만큼 양분 숫자 감소 -> 나이가 1 증가 -> 만약 양분 부족 없어짐
여름: 죽은 나무가 양분으로 -> 죽은 나무 나이 // 2 나무가 있던 칸 양분 추가
가을: 나무의 나이가 5의 배수 age % 5 == 0 -> 인전한 8개의 칸에 나이가 1인 나무가 생긴다.
겨울: 양분이 추가 된다. 입력으로 주어진다.
'''

def spring(ground, trees):
    for i in range(n):
        for j in range(n):
            for idx in range(len(trees[i][j])):
                age = trees[i][j][idx]
                if ground[i][j] - age >= 0:
                    ground[i][j] -= age
                    trees[i][j][idx] += 1
                else:
                    for _ in range(idx, len(trees[i][j])):
                        # 만약 나무가 죽는다면 가장 나이가 적은 나무부터 양분을 먹는데
                        # 이후 나무들은 무조건 현재보다는 나이가 많으므로 이후 나무들도 모두 죽는다.
                        dead_trees[i][j].append(trees[i][j].pop())
                    break


    # for key in trees.keys():
    #     y, x = map(int, key.split('_'))
    #     # trees[key]에는 리스트가 있다.
    #     for idx in range(len(trees[key])):
    #         age = trees[key][idx]
    #         if ground[y][x] - age >= 0:
    #             ground[y][x] -= age
    #             trees[key][idx] += 1
    #         else:
    #             if key in dead_trees.keys():
    #                 dead_trees[key].append(age)
    #             else:
    #                 dead_trees[key] = [age]

            # if ground[y][x] - trees[key] >= 0:
            #     ground[y][x] -= trees[key]
            #     trees[key] += 1
            # else:
            #     dead_trees[key] = trees[key]


def summer(ground, dead_trees, trees):
    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                ground[i][j] += dead_trees[i][j].pop() // 2

    # for key in dead_trees.keys():
    #     for idx in range(len(dead_trees[key])):
    #         y, x = map(int, key.split('_'))
    #         ground[y][x] += dead_trees[key][idx] // 2
    #         trees[key].remove(dead_trees[key][idx])
    #         # trees {'0_0': []} 현상 막기 위해 아래 작업 수행
    #         if len(trees[key]) == 0:
    #             trees.pop(key)

        # y, x = map(int, key.split('_'))
        # ground[y][x] += (dead_trees[key] // 2)
        # trees.pop(key)

'''
1 1 1
1 0 1
1 1 1
'''


def watch_tree(trees):
    for_printing = [[[] for _ in range(n)] for _ in range(n)]

    for key in trees.keys():
        y, x = map(int, key.split('_'))
        for idx in range(len(trees[key])):
            age = trees[key][idx]
            for_printing[y][x].append(age)

    for i in for_printing:
        print(i)
    print()


dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def plant_tree(y, x, trees):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            trees[ny][nx].appendleft(1)
            # key = make_key(ny, nx)
            # if key in trees:
            #     trees[key].append(1)
            # else:
            #     trees[key] = [1]


def fall(trees):
    # 가을: 나무의 나이가 5의 배수 age % 5 == 0
    # 인전한 8개의 칸에 나이가 1인 나무가 생긴다.
    # temp = list(trees.keys())

    for i in range(n):
        for j in range(n):
            for idx in range(len(trees[i][j])):
                if trees[i][j][idx] % 5 == 0:
                    plant_tree(i, j, trees)

    # for key in temp:
    #     for idx in range(len(trees[key])):
    #         age = trees[key][idx]
    #         if age % 5 == 0:
    #             y, x = map(int, key.split('_'))
    #             plant_tree(y, x, trees)

        # if trees[key] % 5 == 0:
        #     y, x = map(int, key.split('_'))
        #     check(y, x, trees)

    # watch_tree(trees)


def winter(s2d2):
    for i in range(n):
        for j in range(n):
            ground[i][j] += s2d2[i][j]

for _ in range(k):
    # for key in trees.keys():
    #     trees[key].sort()

    spring(ground, trees)
    summer(ground, dead_trees, trees)

    fall(trees)
    winter(s2d2)
#
# for i in trees:
#     print(i, trees[i])
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)