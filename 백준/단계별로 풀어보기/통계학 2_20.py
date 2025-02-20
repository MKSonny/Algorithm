import sys

n = int(sys.stdin.readline())
numbers = []
numbers_cnt = {}
total = 0

for _ in range(n):
    number = int(sys.stdin.readline())
    total += number
    numbers.append(number)

    if number not in numbers_cnt.keys():
        numbers_cnt[number] = 1
    else:
        numbers_cnt[number] += 1

maxx, minn = max(numbers), min(numbers)

numbers_cnt = list(numbers_cnt)
print(numbers_cnt)

print(total // n)
numbers.sort()
print(numbers[n // 2])

print(maxx - minn)