self_number = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

total = sorted(self_number - generated_num)

for key in total:
    print(key)