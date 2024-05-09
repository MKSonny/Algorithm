def solution(files):
    # files = ['foo9.txt', 'foo010bar020.zip', 'F-15']
    answer = []
    heads = []
    numbers = []
    tails = []
    idx = 0
    for file_name in files:
        head = ''
        number = ''
        tail = ''
        flag = False
        toggle = False
        for c in file_name:
            if flag and toggle == flag:
                tail += c
                continue
            if c.isdigit():
                number += c
                flag = True
            else:
                if flag:  # 숫자 한번 찍음
                    toggle = True
                    tail += c
                    continue
                head += c.upper()

        heads.append(head)
        numbers.append(int(number))
        tails.append(tail)

        #         heads.append((head, idx))
        #         numbers.append((int(number), idx))
        #         tails.append((tail, idx))
        idx += 1

    new = []
    for i in range(len(files)):
        new.append((heads[i], numbers[i], tails[i], i))

    # heads.sort()
    # numbers.sort()

    new = sorted(new, key=lambda x: (x[0], x[1]))
    temp = []

    for i in new:
        temp.append(files[i[3]])
    answer = temp
    #     print(heads)
    #     print(numbers)
    #     print(tails)

    return answer