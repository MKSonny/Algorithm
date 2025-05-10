from itertools import combinations


def solution(n, q, ans):
    answer = 0

    l = [i for i in range(1, n + 1)]
    c = combinations(l, 5)

    def check(i):
        # combi is still
        for idx, test in enumerate(q):
            cnt = 0

            for i_i in i:
                for t_i in test:
                    if i_i == t_i:
                        cnt += 1

            if cnt != ans[idx]:
                return False

        return True

    for i in c:
        if check(list(i)):
            answer += 1

    return answer