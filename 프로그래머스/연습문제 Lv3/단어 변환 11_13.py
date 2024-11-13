from collections import deque


def solution(begin, target, words):
    answer = 0

    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)

    while q:
        w, cnt = q.popleft()

        if w == target:
            return cnt

        for idx, word in enumerate(words):
            diff = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    diff += 1
            if diff == 1 and visited[idx] != True:
                q.append((word, cnt + 1))
                visited[idx] = True

    return answer