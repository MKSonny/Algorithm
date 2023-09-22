# str = "t0e0a1c2h0er"
str = 'g0en2Ts8eSoft'
n = len(str)
temp = []
for i in range(n):
    if str[i].isdigit():
        temp.append(int(str[i]))

j = 0
while temp[j] == 0:
    print(temp[j])
    temp.pop(j)

n = len(temp)
print(temp)
new_num = 0

for i in range(n):
    new_num += temp[i] * 10 ** ((n - 1) - i)

cnt = 0

for i in range(1, new_num + 1):
    if new_num % i == 0:
        cnt += 1
        print(i, end=' ')

print(new_num, cnt)