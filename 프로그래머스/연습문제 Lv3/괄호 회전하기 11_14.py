from collections import deque


def solution(s):
    answer = 0

    s = deque(s)

    for _ in range(len(s)):
        stack = []

        for i in s:
            if len(stack):
                if stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '(' and i == ')':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        s.append(s.popleft())

        if len(stack) > 0:
            continue

        answer += 1

    return answer