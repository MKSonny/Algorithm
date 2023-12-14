import heapq

label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]

def huff(label, freq):
    h = []
    for i in range(len(label)):
        heapq.heappush(h, (freq[i], label[i]))

    for i in range(len(label) - 1):
        e1 = heapq.heappop(h)
        e2 = heapq.heappop(h)
        heapq.heappush(h, (e1[0] + e2[0], e1[1] + e2[1]))
        print(e1, '+', e2)

    print(heapq.heappop(h))

huff(label, freq)