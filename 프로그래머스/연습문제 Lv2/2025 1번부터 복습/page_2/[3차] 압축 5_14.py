def solution(msg):
    answer = []

    msg = list(msg)

    di = {}

    for i in range(65, ord('Z') + 1):
        di[chr(i)] = i - 65 + 1

    idx = 0
    last = 27

    t_idx = 0

    while t_idx < len(msg):
        w = ''

        while idx < len(msg):
            w += msg[idx]

            if w not in di.keys():
                di[w] = last
                last += 1
                answer.append(di[w[:-1]])
                break

            idx += 1

        if idx == len(msg):
            answer.append(di[w])

        t_idx = idx

    return answer