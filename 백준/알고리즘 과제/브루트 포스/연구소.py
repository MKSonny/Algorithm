# 한 줄씩 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 두 개의 정수를 공백으로 구분하여 입력 받음

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))  # 각 줄에서 숫자들을 공백으로 구분하여 리스트로 변환
    matrix.append(row)
