string = "()(((()())(())()))(())"
map_string = list(map(str, string))
stack = []
poll = 0
cnt = 0
cut = 0

while map_string:
    char = map_string.pop()
    if char == ')':
        stack.append(char)
    else:
        stack.pop()
        cnt += len(stack)

print(poll)
print(cnt)