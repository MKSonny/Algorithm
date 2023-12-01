n, m = map(int, input().split())
password = input().split(' ')
# print(password)
password.sort()
# print(password)

vowels = list('aeiou')
'''
설명
수업시간에 배운 부분합과 유사한 문제다. 
만약 solution의 길이가 k 즉, 4자리 수가 된다면 바로 비밀번호를 인쇄하는 것이 아니라
문제의 조건 자음이 하나 이상 모음이 두 개이상을 만족하는지 검사하는 is_safe_password 함수를 통해
만약 조건을 만족하지 않는다면 백트래킹하여 다음 조합을 검사하도록 한다.
강의 시간의 부분집합 문제에서 dfs로 Combination을 구하는 방법과  N-Queen, 미로찾기 문제에서의 isSafe를 활용하는 문제다.
'''
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