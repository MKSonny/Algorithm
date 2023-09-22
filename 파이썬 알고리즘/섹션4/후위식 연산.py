string = input("str>>>")
str_list = list(map(str, string))
stack = []
res = ''

for item in str_list:
    if item.isnumeric():
        stack.append(item)
    else:
        if item == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        elif item == '-':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b - a)
        elif item == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b * a)
        elif item == '/':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b // a)
print(stack.pop())