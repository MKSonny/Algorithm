n = int(input())
l = []

'''
5
172 67
183 65
180 70
170 72
181 60
'''

for _ in range(n):
    height, weight = map(int, input().split())
    l.append((height, weight))

l.sort(key=lambda o:(o[1], o[0]), reverse=True)

# print(l)

et = 0
cnt = 0

for height, weight in l:
    if et < height:
        et = height
        cnt += 1

print(cnt)