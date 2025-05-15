from collections import deque


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0

        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
            if len(progresses) == 0: break

        answer.append(cnt)

    return answer