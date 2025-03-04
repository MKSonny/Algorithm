'''
5
1 2 3 1 2

1
1 2
1 2 3
1 2 3 1
1 2 3 1 2

2 3 1 2

3 1 2
1 2
2

2
2 3
2 3 1

같은 길이일 경우만 겹칠 수 있음
1 #
2
3
1
2 #

1 2 #
2 3
3 1
1 2 #

1 2 3 #
2 3 1
3 1 2 #

1 2 3 1 #
2 3 1 2 #


1 2 3 1 2 #
'''
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

answer = 0
start, end = 0, 0
seq = [False for _ in range(1000001)]

while start < n and end < n:
    if not seq[l[end]]:
        seq[l[end]] = True
        end += 1
        answer += (end - start)
    else:
        seq[l[start]] = False
        start += 1

print(answer)