def solution(number, k):
    answer = []

    for num in number:
        if len(answer) == 0:
            answer.append(num)
            continue

        while answer[-1] < num and k > 0:
            answer.pop()
            k -= 1

            if not answer:
                break

        answer.append(num)

    if k != 0:
        answer = answer[:-k]

    return ''.join(answer)