index = int(input())

stack = []

for i in range(index):
    string = list(input().split())
    order = string[0]
    # push, pop, size, top, empty
    if order == 'push':
        value = string[1]
        stack.append(value)

    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

