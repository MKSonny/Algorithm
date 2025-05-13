def solution(elements):
    answer = set()

    n = len(elements)
    elements *= 2

    for w_s in range(1, n + 1):
        for i in range(n):
            answer.add(sum(elements[i:i + w_s]))

    return len(answer)