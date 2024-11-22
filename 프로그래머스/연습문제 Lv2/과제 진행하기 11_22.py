from collections import deque
from datetime import datetime, timedelta


def solution(plans):
    answer = []
    plans.sort(key=lambda o: o[1])
    plans = deque(plans)
    times = set()
    format = "%H:%M"  # 시간 포맷

    for i in plans:
        times.add(datetime.strptime(i[1], format))

    not_fin = []
    start_time = plans[0][1]
    # print(start_time)

    cnt = 0

    title, time, left = plans.popleft()

    time = datetime.strptime(time, format)
    left = int(left)

    while left:
        time += timedelta(minutes=1)
        left -= 1
        # print(time, left, not_fin, title)
        # 다른 과제할 시간이 됬고 완료하지 못했다면
        if time in times and left > 0:
            not_fin.append((title, left))
            # 다른 과제로 전환
            title, t_time, left = plans.popleft()
            left = int(left)
        elif time in times and left == 0:
            answer.append(title)
            title, t_time, left = plans.popleft()
            left = int(left)
        elif time not in times and left == 0:
            answer.append(title)
            if len(not_fin) == 0:
                continue
            title, left = not_fin.pop()
            # print(title, left)

    return answer