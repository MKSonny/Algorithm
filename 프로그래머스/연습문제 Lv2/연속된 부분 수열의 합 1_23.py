def solution(sequence, k):
    answer = []

    # 처음 start = 0, end = 0 : 처음부터 끝까지 모두 더했을 경우
    # 만약 check(start, end)가 k보다 작다면
    # start의 크기를 mid + 1 값으로 변경
    # 작다면 end의 크기를 mid - 1 값으로 변경

    # [1, 2, 3, 4, 5]
    # start = 0, end = 4 모두 더하면 15로 k(7)보다 크다.
    # 따라서 end의 크기를 2 - 1 + 1로 변경
    # start = 0 end = 2 모두 더하면 6으로 k보다 작다.
    # start의 값을 mid + 1
    # 이분 탐색 실패

    # [1, 2, 3, 4, 5]에서 뒤부터 가장 작게 1씩 묶어서 탐색한다.
    # 그리고 만약 찾았다면(3, 4) 해당 idx를 answer 배열에 추가한다.

    flag = False

    n = len(sequence) - 1

    for window_size in range(1, len(sequence) + 1):

        # [1, 2, 3, 4, 5]
        # 2

        # 0, 1, 2
        # 4 - 0, 4 - 1 , 4 - 2
        # 4, 3, 2
        idx = 0

        while idx <= len(sequence) // 2:

            if k == sum(sequence[idx:idx + window_size]):
                # print('a', sequence[idx:idx + window_size])
                answer.append([idx, idx + window_size - 1])
                flag = True
                break

            if k == sum(sequence[n - idx:n - idx + window_size]):
                answer.append([n - idx, n - idx + window_size - 1])
                flag = True
                break

            idx += 1

        if flag: break

    answer.sort()
    # print(answer)

    return answer[0]