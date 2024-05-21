import sys

l = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
order = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    order.append(a)

# print(order)

cursor = len(l)

stack_2 = []

for i in order:
    o = list(i.split())
    if o[0] == 'P':
        l.append(o[1])
    elif o[0] == 'L':
        if l:
            stack_2.append(l.pop())
    elif o[0] == 'B':
        if l:
            l.pop()
    elif o[0] == 'D':
        if stack_2:
            l.append(stack_2.pop())

l.extend(reversed(stack_2))
print(''.join(l))