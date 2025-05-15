cnt = 0
answer = 0


def solution(word):
    # answer = 0

    di = ['A', 'E', 'I', 'O', 'U']

    def dfs(level, temp, idx):
        global cnt, answer
        cnt += 1

        # if ''.join(temp) == word:
        # print(''.join(temp), word)
        # print(cnt)
        if level == 5:
            # print(temp)
            return

        for i in di:
            temp.append(i)
            # print(''.join(temp) == word)
            if ''.join(temp) == word:
                # print(cnt)
                answer = cnt
            dfs(level + 1, temp, i)
            temp.pop()

    dfs(0, [], 65)

    return answer