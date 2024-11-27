def solution(files):
    answer = []

    def split_file_name(name, where):
        l = [[] for _ in range(4)]
        idx = 0
        for i in range(len(name)):
            if name[i].isdigit():
                if idx == 0:
                    idx += 1
                l[idx].append(name[i])
            else:
                # if name[i].isalpha() or name[i] == '.' or name[i] == '-':
                if idx != 0:
                    break
                l[idx].append(name[i].upper())
        l[0] = ''.join(l[0])
        l[1] = int(''.join(l[1]))
        l[2] = where
        l[3] = where

        return l

    temp = []
    for idx, i in enumerate(files):
        temp.append(split_file_name(i, idx))
    temp.sort()
    # temp.sort(key=lambda o: (o[0], o[1], o[3]))

    # for i in temp:
    #     print(i)

    for i in temp:
        answer.append(files[i[3]])

    return answer