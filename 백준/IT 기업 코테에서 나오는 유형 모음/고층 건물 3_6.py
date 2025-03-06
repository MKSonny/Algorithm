import sys
from collections import deque

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
# l *= 2
# n *= 2
# l += l[:n//2 + 1]
# n += n//2 + 1

# print(l)

for i in range(n - 1):
    start = i
    end = start + 1

    idx = 0

    total = deque()
    max_total = 0

    # print(start, end)

    while start < n:
        cnt = 1

        while end < n and l[start] > l[end]:
            end += 1
            cnt += 1


        print(cnt, start, end)
        # print(start, end)
        start = end
        end = start + 1

        if end >= n:
            cnt -= 1

        # print(cnt, start, end)

        total.append(cnt)

        idx += 1

        if idx == 1: continue
        else:
            # print('total', total)
            # print(i, sum(total))
            max_total = max(max_total, sum(total))
            # print(sum(total))
            total.popleft()

print(max_total)
'''
[1, 5, 3, 2, 6, 3, 2, 6, 4, 2, 5, 7, 3, 1, 5]
               idx cur
1
'''