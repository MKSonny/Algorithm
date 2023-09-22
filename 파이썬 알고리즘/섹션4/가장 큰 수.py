num = [5, 2, 7, 6, 8, 2, 3]
stack = []
m = 3

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]

print(stack)