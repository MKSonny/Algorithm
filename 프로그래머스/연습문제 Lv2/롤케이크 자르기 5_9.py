from collections import Counter


def solution(topping):
    answer = 0
    other = set()
    dic = Counter(topping)

    for i in topping:
        other.add(i)
        dic[i] -= 1
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(other):
            answer += 1

    return answer