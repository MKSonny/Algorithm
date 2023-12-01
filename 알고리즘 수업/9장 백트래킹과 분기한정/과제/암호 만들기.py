n, m = map(int, input().split())
password = input().split(' ')
# print(password)
password.sort()
# print(password)

vowels = list('aeiou')

def combination(obj, level, k, sol):
    if len(sol) == k:
        if is_safe_password(sol):
            print_password(sol)
        return

    for i in range(level, len(obj)):
        sol.append(obj[i])
        combination(obj, i + 1, k, sol)
        sol.pop()

def print_password(sol):
    for i in sol:
        print(i, end='')
    print()

def is_safe_password(sol):
    vowels_cnt = 0
    consonant_cnt = 0

    for i in range(len(sol)):
        if sol[i] in vowels:
            vowels_cnt += 1
        else:
            consonant_cnt += 1

    if vowels_cnt >= 1 and consonant_cnt >= 2:
        return True
    else:
        return False

combination(password, 0, n, [])