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

height = []
weight = []
l = []

for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
    # height.append(a)
    # weight.append(b)

answer = []

l.sort(key=lambda o:o[0])

for i in range(n - 1):
    flag = True
    for j in range(i + 1, n):
        # a = l[i][0] < l[j][0]
        # b = l[i][1] < l[j][1]
        if l[i][1] < l[j][1]:
            flag = False
            break
    if flag:
        answer.append((l[i][0], l[i][1]))

answer.append(l[n - 1])

# print(answer)
print(len(answer))