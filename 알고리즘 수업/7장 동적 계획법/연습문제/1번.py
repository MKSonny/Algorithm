'''
사용자로부터 n을 입력받아 n번째 피보나치 수를 메모이게이션과 테이블화의
두 가지 방법 으로 각각 구해 출력하는 프로그램을 작성하라. 
'''

def table_fib(n):
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 2] + table[i - 1]

    return table[n]

def do_table_mem(n):
    mem = [None] * (n + 1)
    return table_mem(n, mem)

def table_mem(n, mem):
    if mem[n] == None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = table_mem(n - 2, mem) + table_mem(n - 1, mem)
    return mem[n]

print(do_table_mem(7))