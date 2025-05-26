from collections import deque


def solution(players, m, k):
    answer = 0

    players = deque(players)
    server = []

    while players:
        a = players.popleft()
        t = m

        for i in range(len(server)):
            server[i] -= 1
            if server[i] > 0:
                t += m

        while a >= t:
            server.append(k)
            answer += 1
            a -= m

    return answer