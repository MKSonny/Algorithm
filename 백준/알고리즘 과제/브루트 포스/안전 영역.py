n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))  # 각 줄에서 숫자들을 공백으로 구분하여 리스트로 변환
    matrix.append(row)

for i in range(n):
    for j in range(n):
        k = matrix[i][j]