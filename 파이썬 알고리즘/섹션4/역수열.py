n = int(input())
l = list(map(int, input().split()))
'''
8
5 3 4 0 2 1 1 0
'''
h = [i for i in range(1, n + 1)]
s = [None for _ in range(n)]
print(h)

for k in l:
    cnt = 0
    i = 0
    while True:
        if s[i] == None:
            cnt += 1
        else:
            i += 1
        i += 1
        if cnt == k:
            s[i] = k
            break

print(s)