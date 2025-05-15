def solution(dirs):
    answer = 0

    y, x = 0, 0

    s = set()
    idx = 1

    v = []

    for idx, i in enumerate(dirs):
        temp = []
        temp.append((y, x))

        if i == 'L':
            x -= 1
        elif i == 'U':
            y += 1
        elif i == 'R':
            x += 1
        elif i == 'D':
            y -= 1

        if x < -5:
            x += 1
            continue
        if x > 5:
            x -= 1
            continue
        if y < -5:
            y += 1
            continue
        if y > 5:
            y -= 1
            continue

        # print(idx + 1, y, x)
        temp.append((y, x))
        temp.sort()

        if temp in v:
            # print('a')
            # print(v)
            # print('temp', temp)
            continue
        # print(temp)
        v.append(temp)
        # print(v)

        answer += 1

    return answer