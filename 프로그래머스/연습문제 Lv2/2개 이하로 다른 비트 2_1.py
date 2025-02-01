def solution(numbers):
    # numbers.append(9)
    # numbers.append(11)
    answer = []

    # 1이 더 많고
    # 1이 더 적다면 앞의 0을 1로 만들어야 됨
    # 1식 더 하면서 검사?
    # print(format(10**15, 'b'))

    def da3(v, ori):

        idx = 0

        for i in range(len(v)):
            if v[i] == '1':
                idx = i
                break

        v = list(v)
        v[0] = '1'
        v[idx] = '0'

        v = ''.join(v)

        # print(v, idx)
        if int(v, 2) > ori:
            return int(v, 2)
        else:
            return float('inf')

    def da2(v, ori):
        idx = 0
        v = list(v)

        # 앞에서부터 가장 큰 0을 1로 만들고
        # 그 뒤에서부터 1을 0으로 만든다
        for i in range(len(v) - 1, -1, -1):
            if v[i] == '0':
                idx = i

                v[i] = '1'
                break

        for i in range(idx + 1, len(v)):
            if v[i] == '1':
                v[i] = '0'
                break

        v = ''.join(v)

        if int(v, 2) > ori:
            return int(v, 2)
        else:
            return float('inf')

    def da(f, s):

        if len(f) > len(s):
            s = '0' + s
        elif len(f) < len(s):
            f = '0' + f

        cnt = 0

        for i in range(len(f)):
            if f[i] != s[i]:
                cnt += 1

        return cnt

    def check(v, i):
        c = 3

        # 01011 -> 11

        # 01111 -> 15

        # 01101 -> 13

        # 01001 -> 9
        # 01010 -> 10
        # 01011 -> 11

        if v[-1] == '0':
            i += 1
            return i
        else:
            # print(da2(v), da3(v))
            return min(da2(v, i), da3(v, i))

        while c > 2:
            i += 2
            c = da(v, format(i, 'b'))
            # print(c, v, format(i, 'b'))

        return i

    for i in numbers:
        v = '0' + format(i, 'b')
        answer.append(check(v, i))

    return answer