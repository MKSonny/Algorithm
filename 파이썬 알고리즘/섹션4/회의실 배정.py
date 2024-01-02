n = int(input())
l = []

'''
5
1 4
2 3
3 5
4 6
5 7
'''

for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

# o[1]: 끝나는 시간이 같다면 o[0]을 기준으로 정렬
l.sort(key=lambda o:(o[1], o[0]))

ep = l[0][1]

cnt = 1

for i in range(1, n):
    if ep <= l[i][0]:
        cnt += 1
        ep = l[i][1]

print(cnt)