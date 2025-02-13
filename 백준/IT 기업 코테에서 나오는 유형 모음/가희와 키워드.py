import sys

n, m = map(int, sys.stdin.readline().split())
memo = set()
blogs = []

for _ in range(n):
    memo.add(sys.stdin.readline().rstrip())

for _ in range(m):
    blogs.append(sys.stdin.readline().rstrip().split(','))

for blog in blogs:
    for keyword in blog:
        memo.discard(keyword)
    print(len(memo))