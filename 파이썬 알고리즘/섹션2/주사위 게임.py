n = int(input())
h = []

'''
3
3 3 6 
2 2 2 
6 2 5
'''
for _ in range(n):
    l = [0 for _ in range(6 + 1)]
    a, b, c = map(int, input().split())
    l[a] += 1
    l[b] += 1
    l[c] += 1
    maxx = max(l)
    if maxx == 3:
        h.append(10000 + a * 1000)
    elif maxx == 2:
        for i in range(1, n + 1):
            if maxx == l[i]:
                h.append(1000 + i * 100)
                break
    else:
        h.append(max(a, b, c) * 100)

print(max(h))