def solution(numbers):
    answer = ''

    if max(numbers) == 0:
        return '0'

    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(key=lambda o: o * 3, reverse=True)

    for i in numbers:
        answer += i

    return answer