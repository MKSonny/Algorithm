'''
3. 억지기법과 완전 탐색
    1. 선택 정렬
    2. 순차 탐색
    3. 문자열 매칭
    4. 최근접 쌍의 거리
    5. 완전 탐색
    6. 그래프 탐색 (DFS, BFS)
'''

def string_match(t, p):
    n = len(t)
    m = len(p)
    for i in range(n):
        j = 0
        while t[i + j] == p[j]:
            j += 1
            if j == m:
                return i
    return -1

string = list('hello world')
print(string_match(string, 'el'))

'''
4. 축소 정복 기법 -> 모든 경우의 수(상향식, 하향식)
    1. 삽입 정렬
    2. 위상 정렬
    3. 이진 탐색
    4. 거듭제곱 문제
    5. k번째 작은 수 찾기
5. 분할 정복 기법
    1. 병합 정렬
    2. 퀵 정렬
'''