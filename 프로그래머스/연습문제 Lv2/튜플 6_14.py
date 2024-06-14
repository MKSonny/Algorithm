def solution(s):
    answer = []

    s = list(s)
    s = s[1:-1]

    a = ''
    temp = []

    for i in s:
        if i == '{':
            l = []
            t = ''
        elif i.isdigit():
            t += i
        elif i == ',':
            if t != '':
                l.append(int(t))
            t = ''
        elif i == '}':
            l.append(int(t))
            t = ''
            temp.append(l)

    # print(temp)
    temp.sort(key=lambda o: len(o))
    al = set()
    # print(temp)
    answer.append(temp[0][0])
    al.add(temp[0][0])

    for i in range(1, len(temp)):
        for item in temp[i]:
            if item not in al:
                al.add(item)
                answer.append(item)

    return answer