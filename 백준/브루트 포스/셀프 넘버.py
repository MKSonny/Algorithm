def self_number(n):
    sum = int(n)
    n = list(n)

    for num in n:
        sum += int(num)

    return sum

l = []

for i in range(1, 10001):
    self_result = self_number(str(i))
    if self_result > 10000:
        continue
    l.append(self_result)

for i in range(1, 10001):
    if i in l:
        continue
    print(i)