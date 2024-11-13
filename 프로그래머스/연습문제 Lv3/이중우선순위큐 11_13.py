import heapq


def solution(operations):
    answer = []
    mh = []
    h = []
    q = []

    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(h, int(b))
            heapq.heappush(mh, -int(b))
        elif a == 'D':
            if b == '1':
                if len(mh) == 0:
                    continue
                t = -heapq.heappop(mh)
                if t in h and len(h) != 0:
                    h.remove(t)
            elif b == '-1':
                if len(h) == 0:
                    continue
                t = heapq.heappop(h)
                if -t in mh and len(mh) != 0:
                    mh.remove(-t)
    if len(mh) == 0:
        answer.append(0)
    else:
        answer.append(-heapq.heappop(mh))
    if len(h) == 0:
        answer.append(0)
    else:
        answer.append(heapq.heappop(h))
    return answer