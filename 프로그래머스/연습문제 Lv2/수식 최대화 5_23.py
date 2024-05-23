import re
from itertools import permutations

def solution(expression):
    rank_options = [1, 2, 3]
    maxx = -1
    for i in permutations(rank_options):
        rank = {
            '*': i[0],
            '+': i[1],
            '-': i[2]
        }

        def infix_to_postfix(expression):
            output = []
            stack = []

            l = re.findall(r'\d+|[-+*]', expression)

            for token in l:
                if token.isdigit():
                    output.append(token)
                else:
                    while stack and rank[stack[-1]] >= rank[token]:
                        output.append(stack.pop())
                    stack.append(token)

            while stack:
                output.append(stack.pop())

            return output

        def calulate_postfix(postfix):
            stack = []

            for token in postfix:
                if token.isdigit():
                    stack.append(int(token))
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if token == '+':
                        stack.append(a + b)
                    elif token == '-':
                        stack.append(a - b)
                    elif token == '*':
                        stack.append(a * b)

            return stack[0]


        postfix_expression = infix_to_postfix(expression)

        result = abs(calulate_postfix(postfix_expression))
        maxx = max(maxx, result)

    return maxx