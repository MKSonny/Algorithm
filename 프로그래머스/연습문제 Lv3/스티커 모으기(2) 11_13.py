from collections import deque
import copy


def solution(sticker):
    answer = 0

    l = deque([])

    for idx, item in enumerate(sticker):
        l.append((item, idx))

    q = deque()

    visited = [False] * len(sticker)
    visited[0] = True
    t = copy.deepcopy(sticker)

    q.append((sticker, 0, sticker[0]))

    while q:
        sticker, idx, total = q.popleft()
        temp = sticker[idx]
        print(total)
        sticker.pop(idx - 1)
        sticker.pop(idx - 1)
        sticker.pop(idx - 1)
        c_s = copy.deepcopy(sticker)
        q.append((c_s, total + temp))

    return answer