def solution(cacheSize, cities):
    answer = 0

    cache = ['p'] * cacheSize

    cnt = 0

    if cacheSize == 0:
        return len(cities) * 5

    for c in cities:
        hit = False
        for i in range(cacheSize):
            if cache[i].upper() == c.upper():
                cache.pop(i)
                cache.append(c)
                cnt += 1
                hit = True
                break
        if not hit:
            cache.pop(0)
            cache.append(c)
            # print(cache)
            cnt += 5
        # print(cache, cnt, c)

    return cnt