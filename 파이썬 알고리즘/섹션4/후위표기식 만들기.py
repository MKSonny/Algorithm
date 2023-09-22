string = input("str>>>")
str_list = list(map(str, string))
prior = {"+": 1, "-": 1, "*": 2, "/": 2}
stack = []
res = ''

for item in str_list:
    if item.isnumeric():
        res += item
    else:
        if item == '(':
            stack.append(item)
        elif item == '*' or item == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(item)
        elif item == '+' or item == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(item)
        elif item == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)