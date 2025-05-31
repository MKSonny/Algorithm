def solution(arrayA, arrayB):
    answer = [0]

    l = arrayA + arrayB

    lt = 0
    rt = len(l) - 1

    for idx in range(2, min(arrayA) + 1):
        lt = 0
        rt = len(l) - 1
        cnt = 0

        while l[lt] % idx == 0 and l[rt] % idx != 0:
            lt += 1
            rt -= 1
            cnt += 1

        if cnt == len(arrayA):
            answer.append(idx)

    for idx in range(2, min(arrayB) + 1):
        lt = 0
        rt = len(l) - 1
        cnt = 0

        while l[lt] % idx != 0 and l[rt] % idx == 0:
            lt += 1
            rt -= 1
            cnt += 1

        if cnt == len(arrayA):
            answer.append(idx)

    return max(answer)