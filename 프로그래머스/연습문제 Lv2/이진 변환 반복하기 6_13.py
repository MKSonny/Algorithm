from collections import Counter


def to_(num):
    s = ''
    while num:
        s += str(num % 2)
        num //= 2
    return s


def solution(s):
    answer = []

    d = 0
    cnt = 0

    while True:
        c = Counter(s)
        cnt += 1
        d += c['0']
        if c['1'] == 1:
            break
        s = to_(c['1'])

    return [cnt, d]