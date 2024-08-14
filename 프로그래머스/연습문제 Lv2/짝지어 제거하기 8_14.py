def solution(s):
    answer = -1

    temp = []

    for i in s:
        if len(temp) != 0 and i == temp[-1]:
            temp.pop()
        else:
            temp.append(i)

    if len(temp) == 0:
        return 1
    else:
        return 0