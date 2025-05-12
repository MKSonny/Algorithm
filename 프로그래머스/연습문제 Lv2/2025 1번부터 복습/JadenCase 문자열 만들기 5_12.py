def solution(s):
    answer = ''

    s = list(s)

    idx = 0

    flag = True

    while idx < len(s):
        if flag and s[idx] != ' ':
            answer += str.upper(s[idx])
            flag = False
            idx += 1
            continue

        if s[idx] == ' ':
            flag = True

        answer += str.lower(s[idx])

        idx += 1

    return answer