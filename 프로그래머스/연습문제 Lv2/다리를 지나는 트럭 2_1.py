from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    # deque에 truck_weights 빼고 추가함
    # deque sum이 다음 트럭이 들어올때 weight를 넘는다면 7이 빠질때까지 기다린다
    # 빠졌다면 추가, weight를 넘지 않고 bridge_length가 넘지 않는다면
    # 다음 트럭 추가, 반복

    # 시간 구현 위해 deque의 길이를 bridge_length로 설정

    b = deque([0 for _ in range(bridge_length)])
    t = deque(truck_weights)

    total = 0

    # 0, 0

    while True:
        total -= b.popleft()
        flag = False

        answer += 1

        if t and total + t[0] <= weight:
            w = t.popleft()
            b.append(w)
            flag = True
            total += w

        if flag == False:
            b.append(0)

        if total == 0:
            break

    return answer