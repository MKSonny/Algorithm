n = int(input())
l = list(map(int, input().split()))
'''
10 
45 73 66 87 92 67 75 79 75 80
'''
# base = round(sum(l) / n)
base = int((sum(l) / n) + 0.5)
# 기존 round 방식은 round_half_even 방식을 택한다.
# round_half_even 방식은 4.500일 경우
# round(4.500)의 결과는 4.5가 나온다.
# 따라서 a = 4.5이면 a += 0.5를 한 이후
# a = int(a)로 반올림을 처리한다.

h = []
for value in l:
    h.append(abs(value - base))

dis = min(h)
tmp = []
for i in range(n):
    if dis == h[i]:
        tmp.append((i + 1, l[i]))

# print(tmp)
maxx = max(tmp, key=lambda o:o[1])
# print(maxx[1])
for i in tmp:
    if i[1] == maxx[1]:
        print(base, i[0])
        break