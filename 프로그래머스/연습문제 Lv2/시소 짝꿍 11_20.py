from collections import Counter


def solution(weights):
    answer = 0

    counter = Counter(weights)
    for k, v in counter.items():
        if v >= 2:
            # 같은 값이 3개라면
            # 총 경우의 수 -> 3 * 2
            # 중복 제거 -> // 2
            answer += v * (v - 1) // 2

    weights = set(weights)

    for w in weights:
        # 180
        if w * 2 / 3 in weights:
            answer += counter[w * 2 / 3] * counter[w]
        if w * 2 / 4 in weights:
            answer += counter[w * 2 / 4] * counter[w]
        if w * 3 / 4 in weights:
            answer += counter[w * 3 / 4] * counter[w]

    return answer