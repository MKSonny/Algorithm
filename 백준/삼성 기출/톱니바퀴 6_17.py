import sys
from collections import deque

l = deque()

for _ in range(4):
    l.append(deque(list(sys.stdin.readline().rstrip())))

n = int(sys.stdin.readline())

how = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    how.append((a - 1, b))

def dfs_check_right(num, clock, l):
    if num == 3:
        return
    # if l[num][2] != l[num - 1][-2]:
    #     if clock == 1:
    #         l[num - 1].append(l[num].popleft())
    #     else:
    #         l[num - 1].appendleft(l[num].pop())
    # print(l)
    # print(num, num + 1, 'a', l[num][2], l[num + 1][-2])
    # print()
    if l[num][2] != l[num + 1][-2]:
        if clock == 1:
            l[num + 1].append(l[num + 1].popleft())
            clock = 0
        else:
            l[num + 1].appendleft(l[num + 1].pop())
            clock = 1

    dfs_check_right(num + 1, clock, l)

def dfs_check_left(num, clock, l):
    # print(num)
    if num == 0:
        return
    if l[num][2] != l[num - 1][-2]:
        if clock == 1:
            l[num - 1].append(l[num - 1].popleft())
            clock = 0
        else:
            l[num - 1].appendleft(l[num - 1].pop())
            clock = 1
    # if l[num][2] != l[num + 1][-2]:
    #     if clock == 1:
    #         l[num + 1].append(l[num].popleft())
    #     else:
    #         l[num - 1].appendleft(l[num].pop())
    dfs_check_left(num - 1, clock, l)



    # dfs_rotate(num - 1, clock, l)


for num, clock in how:
    # for i in l:
    #     print(i)
    # print()

    if clock == 1:
        dfs_check_left(num, clock, l)
        dfs_check_right(num, clock, l)
        l[num].appendleft(l[num].pop())
    else:
        dfs_check_left(num, clock, l)
        dfs_check_right(num, clock, l)
        l[num].append(l[num].popleft())

    for i in l:
        print(i)
    print()


score = [1, 2, 4, 8]
answer = 0

# for i in l:
#     print(i)

for i in range(4):
    answer += int(l[i][0]) * score[i]
print(answer)