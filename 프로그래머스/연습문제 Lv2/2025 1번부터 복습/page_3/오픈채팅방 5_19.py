def solution(record):
    answer = []

    di = {}

    for i in record:
        l = list(i.split())

        if len(i) > 2:
            if l[0] == 'Enter':
                if l[1] not in di.keys():
                    di[l[1]] = l[2]
                else:
                    di[l[1]] = l[2]
            elif l[0] == 'Change':
                di[l[1]] = l[2]

    for i in record:
        l = list(i.split())

        if len(l) > 2:
            if l[0] == 'Enter':
                answer.append(di[l[1]] + '님이 들어왔습니다.')
        else:
            answer.append(di[l[1]] + '님이 나갔습니다.')

    return answer