def solution(n, words):
    answer = []

    before, now = 0, 1
    spoke = [words[0]]

    last_idx = 0
    flag = True

    for i in range(1, len(words)):
        if words[i] in spoke:
            flag = False
            break

        if words[i - 1][-1] != words[i][0]:
            flag = False
            break

        last_idx = i
        spoke.append(words[i])

    if flag: return [0, 0]

    last_idx += 1
    return [last_idx % n + 1, last_idx // n + 1]

    return answer