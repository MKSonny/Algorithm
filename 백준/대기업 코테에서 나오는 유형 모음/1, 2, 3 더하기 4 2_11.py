# 60
import sys
from itertools import combinations
from telnetlib import theNULL

n = int(sys.stdin.readline())

lo = []

for _ in range(n):
    lo.append(int(sys.stdin.readline()))

# 1
# 1

# 2
# 1 + 1
# 2

# 3
# 1 + 1 + 1
# 1 + 2
# 3

# 4
# 1 + 1 + 1 + 1
# 2 + 1 + 1
# 2 + 2
# 3 + 1

# 5
# 1 + 1 + 1 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 3 + 2

# 4 + 1
test = [2, 3]

te = [1 for _ in range(4)]
total = sum(te)
total -= te.pop()
for i in test:


