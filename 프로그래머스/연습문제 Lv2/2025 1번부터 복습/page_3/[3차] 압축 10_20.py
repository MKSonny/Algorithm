def solution(msg):
    answer = []

    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    al = list(al)

    di = {}

    for i in range(len(al)):
        di[al[i]] = i + 1

    last = 27

    temp = msg[0]
    key_number = -1
    i = 0
    prv = ""

    while i < len(msg):
        if temp in di:
            if i < len(msg) - 1:
                i += 1
            else:
                answer.append(di[temp])
                break
            temp += msg[i]
        else:
            di[temp] = last
            answer.append(di[temp[:-1]])
            last += 1
            temp = msg[i]
        # i += 1

    # print(di)

    return answer