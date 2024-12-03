from itertools import product


def solution(users, emoticons):
    answer = []

    sale = [10, 20, 30, 40]

    def check(users, sol):
        all_total = 0
        sign_total = 0
        for buy_if, sign_if in users:
            total = 0
            flag = False
            for idx, sale in enumerate(sol):
                if sale >= buy_if:
                    total += (emoticons[idx] * ((100 - sale) / 100))
            if total >= sign_if:
                sign_total += 1
            else:
                all_total += int(total)
        return sign_total, all_total

    max_users = 0
    max_total = 0

    def dfs(level, sol):
        nonlocal max_users
        nonlocal max_total
        if level == len(emoticons):
            u, t = check(users, sol)
            if u > max_users:
                max_users = u
                max_total = t
            elif u == max_users:
                max_users = u
                max_total = max(t, max_total)
            return
        for i in range(4):
            sol.append(sale[i])
            dfs(level + 1, sol)
            sol.pop()

    dfs(0, [])

    return [max_users, max_total]