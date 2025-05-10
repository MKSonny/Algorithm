def solution(s):
    answer = ''

    l = list(map(int, s.split()))

    answer += str(min(l)) + ' ' + str(max(l))

    return answer