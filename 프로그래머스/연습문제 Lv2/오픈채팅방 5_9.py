def solution(record):
    answer = []
    d = {}

    for i in record:
        a = i.split()
        if a[0] == 'Enter':
            if d.get(a[1]) == None:
                d[a[1]] = a[2]
            d[a[1]] = a[2]
        elif a[0] == 'Change':
            d[a[1]] = a[2]
        # print(i)

    msg = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}

    # print(d)

    for i in record:
        a = i.split()
        if a[0] == 'Change':
            continue
        answer.append(d[a[1]] + '님이 ' + msg[a[0]])

    return answer