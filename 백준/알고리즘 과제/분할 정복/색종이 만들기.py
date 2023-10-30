n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

cnt = 0

# n = 4
# x = 0, y = 0
# i: 0 ~ 3 , j: 0 ~ 3
# i: 0 ~ 3 , j: 4 ~ 7
# i: 4 ~ 7 , j: 0 ~ 3
# i: 4 ~ 7 , j: 4 ~ 7

my_dict = {
    0: 0,
    1: 0
}

def paper_split(y, x, n):
    global white, blue

    # 처음 시작점의 종이 색깔, 0 or 1
    color = matrix[y][x]

    for i in range(y, y + n):
        for j in range(x, x + n):
            if color != matrix[i][j]:
                mid = n // 2
                paper_split(y, x, mid)
                paper_split(y, x + mid, mid)
                paper_split(y + mid, x, mid)
                paper_split(y + mid, x + mid, mid)
                # 여기에 return을 하지 않으면
                # 다른 색깔이 섞여있어도 for 문이 모두 끝난후
                # paper_split가 호출되는 만큼 my_dict 값이 증가한다.
                return

    # 여기까지 왔다는 것은 모두 같은 색이었다는 것
    my_dict[color] += 1


paper_split(0, 0, n)
print(my_dict[0])
print(my_dict[1])