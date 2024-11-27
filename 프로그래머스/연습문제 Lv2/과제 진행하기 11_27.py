from collections import deque


def get_int(plan):
    subject, start, playtime = plan

    a, b = start.split(":")

    start = int(a) * 60 + int(b)

    playtime = int(playtime)

    return subject, start, playtime


def solution(plans):
    answer = []

    plans.sort(key=lambda x: x[1])

    st = []

    plans_idx = 1

    now_subject, now_start, now_playtime = get_int(plans[0])

    while 1:
        next_subject, next_start, next_playtime = get_int(plans[plans_idx])

        if next_start < now_start + now_playtime:
            st.append((now_subject, now_start + now_playtime - next_start))
            now_subject, now_start, now_playtime = next_subject, next_start, next_playtime
            plans_idx += 1

        else:
            answer.append(now_subject)

            if st:
                if next_start == now_start + now_playtime:
                    now_subject, now_start, now_playtime = next_subject, next_start, next_playtime
                    plans_idx += 1
                else:
                    subject, remain_playtime = st.pop()
                    now_subject, now_start, now_playtime = subject, now_start + now_playtime, remain_playtime

            else:
                now_subject, now_start, now_playtime = next_subject, next_start, next_playtime
                plans_idx += 1

        if plans_idx == len(plans):
            answer.append(now_subject)
            break

    for subject, _ in st[::-1]:
        answer.append(subject)

    return answer