def solution(order):
    answer = 0
    l = []
    idx = 0
    num = 0
    n = len(order)
    stack = []
    while idx < n:
        if order[idx] > num:
            num += 1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx

    return idx