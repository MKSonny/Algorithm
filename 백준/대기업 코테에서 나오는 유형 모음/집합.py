import copy
import sys

n = int(sys.stdin.readline())
l = set()

for _ in range(n):
    order = sys.stdin.readline().rstrip().split()

    if len(order) > 1:
        order_str = order[0]
        order_num = int(order[1])
    else:
        order_str = order[0]
        if order_str == 'all':
            l = set(i for i in range(1, 21))
        else:
            l = set()

    if order_str == 'add':
        l.add(order_num)
    elif order_str == 'remove':
        l.discard(order_num)
    elif order_str == 'check':
        print(1 if order_num in l else 0)
    elif order_str == 'toggle':
        if order_num in l:
            l.discard(order_num)
        else:
            l.add(order_num)
