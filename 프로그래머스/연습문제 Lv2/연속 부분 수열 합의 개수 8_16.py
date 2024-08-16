def solution(elements):
    answer = 0

    n = len(elements)
    elements *= n
    temp = set()

    for j in range(1, n):
        for i in range(n):
            temp.add(sum(elements[i:i + j]))

    return len(temp) + 1