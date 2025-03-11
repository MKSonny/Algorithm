import sys

n = int(sys.stdin.readline())
words = [(sys.stdin.readline().strip(), i) for i in range(n)]
prefix = ''
answer_min_idx = float('inf')
