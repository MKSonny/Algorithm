def solution(files):
    answer = []

    answer = []

    for k, file in enumerate(files):

        idx = 0
        head = ''
        number = ''
        tail = ''

        while idx < len(file):
            if ord(file[idx]) < ord('0') or ord(file[idx]) > ord('9'):
                head += str.upper(file[idx])
            else:
                break
            idx += 1

        while idx < len(file):
            if ord('0') <= ord(file[idx]) <= ord('9'):
                number += file[idx]
            else:
                break
            idx += 1

        while idx < len(file):
            tail += file[idx]
            idx += 1

        answer.append((head, int(number), k))
        # print('head', head)
        # print('number', number)
        # print('tail', tail)
        # print()

    answer.sort()

    temp = []

    for a, b, idx in answer:
        temp.append(files[idx])

    return temp