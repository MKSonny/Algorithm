def solution(n, m, section):
    answer = 0

    section.sort()

    prev_s, prev_e = section[0], section[0] + m - 1
    answer = 1

    for i in range(1, len(section)):
        if prev_s <= section[i] <= prev_e:
            continue
        else:
            prev_s = section[i]
            prev_e = section[i] + m - 1
            answer += 1

    return answer