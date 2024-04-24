def solution(keymap, targets):
    answer = []

    d = {}

    for i in keymap:
        for idx, key in enumerate(i):
            if not d.get(key):
                d[key] = idx + 1
            else:
                if idx + 1 < d[key]:
                    d[key] = idx + 1

    # print(d)

    for t in targets:
        total = 0
        for i in t:
            if not d.get(i):
                answer.append(-1)
                break
            total += d[i]
        else:
            answer.append(total)

    return answer