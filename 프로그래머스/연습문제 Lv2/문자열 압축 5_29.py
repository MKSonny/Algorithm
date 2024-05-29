def solution(s):
    answer = ''

    n = len(s)

    for i in range(1, n + 1):
        idx = 0
        str_cnt = 0
        o_str = ''
        t_str = ''
        total = 1
        answer = ''

        while idx <= n:
            if idx == n:
                if o_str == t_str:
                    total += 1
                    answer += (str(total) + o_str)
                else:
                    answer += '1' + t_str
                break
            if str_cnt < i:
                t_str += s[idx]
                str_cnt += 1
            else:
                idx -= 1
                str_cnt = 0
                if o_str == t_str:
                    total += 1
                else:
                    answer += (str(total) + o_str)
                    total = 1
                o_str = t_str
                t_str = ''
            idx += 1

        print(i, t_str, o_str, total)
        print(answer[1:])

print(solution('ababcdcdababcdcd'))