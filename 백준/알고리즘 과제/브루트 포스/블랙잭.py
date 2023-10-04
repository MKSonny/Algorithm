n, m = map(int, input().split())
cards = list(map(int, input().split()))

total_list = []
for i in range(n - 2):
    total = 0
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                total_list.append(total)
print(max(total_list))