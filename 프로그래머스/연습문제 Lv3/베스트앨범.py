def solution(genres, plays):
    genres = ["classic", "pop", "classic", "classic"]
    plays = [600, 600, 600, 700]

    answer = []
    d = {}
    d_sum = {}
    idx = 0
    r_g = set()
    pre_p = - 1
    idx_d = {}

    for genre, play in zip(genres, plays):
        if d.get(genre) == None:
            l = []
            k = []
            d[genre] = l
            idx_d[genre] = k
            d_sum[genre] = 0
            r_g.add(genre)
        d_sum[genre] += play
        d[genre].append(play)
        idx_d[genre].append(idx)

        idx += 1

    print(d)
    print(idx_d)
    # print(r_g)

    # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다
    # ====
    for genre in r_g:
        d[genre].sort()
        idx_d[genre].sort()

    print(d)
    print(idx_d)

    #     rank = []

    #     for s in d_sum:
    #         rank.append(d_sum[s])

    #     rank.sort(reverse = True)
    #     print(rank)

    #     # cnt = 0

    #     # print('d', d)

    #     for r in rank:
    #         for g in r_g:
    #             if d_sum[g] == r:
    #                 cnt = 0
    #                 while cnt < 2:
    #                     if len(d[g]) > 0:
    #                         answer.append(d[g].pop()[1])
    #                         cnt += 1
    #                     else:
    #                         break
    #                     # answer.append(d[g].pop()[1])

    #     print(answer)

    return answer