import re

l = '100-200*300-500+20'
# l = '50*6-3*2'
# temp = ''
# for i in l:
#     if i.isdigit():
#        temp += i
#     else:
#
# result = re.split(r'[-+*]', l)
# print(result)

rank = {
    '*': 3,
    '-': 1,
    '+': 2
}

# rank = {
#     '*': 2,
#     '-': 3,
#     '+': 2
# }


answer = ''
stack = []

for i in l:
    if i.isdigit():
        answer += i
    else:
        if stack and rank[stack[-1]] >= rank[i]:
            answer += '|' + stack.pop() + '|'
            stack.append(i)
        else:
            answer += '|'
            # print(stack, i)
            stack.append(i)
while stack:
    answer += '|' + stack.pop()

stack = []
print(answer)

temp = ''
for i in answer:
    print(stack)
    if i.isdigit():
        temp += i
    elif temp != '' and i == '|':
        stack.append(int(temp))
        temp = ''
    elif not i.isdigit() and i != '|':
        n1 = stack.pop()
        n2 = stack.pop()
        if i == '+':
            stack.append(n1 + n2)
        elif i == '-':
            stack.append(-(n1 - n2))
            # stack.append(-(n1 + n2))
        elif i == '*':
            stack.append(n1 * n2)

print(stack)