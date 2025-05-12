from collections import deque


def solution(s):
    answer = 0

    if len(s) == 1: return 0

    def check(s):
        temp = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                temp.append(i)
            else:
                if len(temp) == 0:
                    return False

                if i == ')' and temp[-1] != '(':
                    return False
                if i == '}' and temp[-1] != '{':
                    return False
                if i == ']' and temp[-1] != '[':
                    return False
                temp.pop()

        if len(temp) > 0: return False

        return True

    s = list(s)
    s = deque(s)

    for i in range(len(s)):
        if check(s): answer += 1
        s.rotate(-1)

    return answer