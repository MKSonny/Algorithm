def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(idx, p)]
        else:
            dic1[g].append((idx, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for g, total_plays in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for idx, p in sorted(dic1[g], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(idx)

    return answer