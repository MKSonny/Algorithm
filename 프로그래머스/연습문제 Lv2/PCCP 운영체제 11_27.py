import heapq


def solution(program):
    answer = [0] * 11
    heap = []

    # 호출된 시간이 가장 우선, 이후 시간이 같다면 우선순위가 낮은 것부터 처리
    program.sort(key=lambda x: (x[1], x[0]))
    time = 0  # 전체 시간

    while program or heap:
        while program and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))

        # 실행 중인 프로그램이 없다면
        if program and not heap:
            # 다음 프로그램의 호출된 시간까지로 이동
            time = program[0][1]
            heapq.heappush(heap, program.pop(0))

        temp = heapq.heappop(heap)
        # temp[1]: 호출된 시간
        answer[temp[0]] += (time - temp[1])
        time += temp[2]  # 현재 시간에 수행 시간을 더한다

    answer[0] = time

    return answer