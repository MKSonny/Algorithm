from collections import Counter


def solution(participant, completion):
    answer = ''

    d = Counter(participant)
    c = Counter(completion)

    return list((d - c).keys())[0]