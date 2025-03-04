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
s = []
