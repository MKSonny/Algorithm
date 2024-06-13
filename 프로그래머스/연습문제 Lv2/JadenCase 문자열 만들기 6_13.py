def solution(s):
    answer = ''

    s = s.split(' ')

    for i in s:
        for c in range(len(i)):
            if c == 0:
                if not i[c].isdigit():
                    answer += i[c].upper()
                else:
                    answer += i[c]
                continue
            if i[c].isupper():
                answer += i[c].lower()
            else:
                answer += i[c]
        answer += ' '
    answer = list(answer)
    answer.pop()
    answer = ''.join(answer)
    return answer