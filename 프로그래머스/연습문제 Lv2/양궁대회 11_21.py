def solution(n, info):
    answer = [0 for _ in range(11)]
    tmp = [0 for _ in range(11)]
    maxDiff = 0

    for subset in range(1, 1 << 10):
        ryan = 0
        appeach = 0
        cnt = 0

        # print(subset)
        for i in range(10):
            if subset & (1 << i):
                ryan += 10 - i
                # 라이언이 쏴야 하는 화살의 수는 어피치보다
                # 하나만 많으면 된다
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                if info[i]:
                    appeach += 10 - i

        if cnt > n: continue
        tmp[10] = n - cnt  # 남은 화살은 0점에 맞춘걸로 기록

        if ryan - appeach == maxDiff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    maxDiff = ryan - appeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
        elif ryan - appeach > maxDiff:
            maxDiff = ryan - appeach
            answer = tmp[:]

    if maxDiff == 0:
        answer = [-1]

    return answer