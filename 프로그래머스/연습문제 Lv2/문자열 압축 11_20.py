from collections import deque


def solution(s):
    answer = 100000
    # s = list(s)
    # for
    if len(s) == 1:
        return 1
    for j in range(1, len(s) - 1):
        prev = s[0:j]
        cnt = 1
        temp = ''
        for i in range(j, len(s) + j, j):
            # print(s[i:i + 2])
            # print(i)
            if prev == s[i:i + j]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt) + prev
                else:
                    temp += prev
                prev = s[i:i + j]
                cnt = 1
        answer = min(len(temp), answer)
    # print(temp)

    return answer