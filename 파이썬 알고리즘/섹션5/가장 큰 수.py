n, m = map(int, input().split())

n = list(str(n))
s = []
cnt = 0
n = [int(i) for i in n]

for i in n:
    if len(s) == 0 or s[-1] >= i:
        s.append(i)
    else:
        while len(s) != 0 and s[-1] < i and cnt != m:
            a = s.pop()
            cnt += 1
        s.append(i)

if cnt != m:
    for _ in range(m - cnt):
        s.pop()
print(s)

'''
5276823 3
9977252641 5
'''