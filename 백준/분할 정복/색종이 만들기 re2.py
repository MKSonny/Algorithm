n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

# def devide(l, n):
    # 4등분 후, 각각 for문을 돌아야 함
    # 그럼 나눌 기준값 8이 있어야 함
    # 위를 n을 기준으로 하면
    # 0, 4, 8 이 3가지 숫자만 있으면 됨
    # 그러면 4 = n // 2, 8 = n
    # 0은 시작 점인데 어떻게 알지..
    # 일단 0도 넘겨야 된다.
    # devide는 검사용?

white = 0
blue = 0

def color(y, x, yn, xn):
    global white
    global blue
    c = l[y][x]
    for i in range(y, yn):
        for j in range(x, xn):
            if c != l[i][j]:
                # devide(0, 4, 8)
                # 1: 0 ~ 4, 0 ~ 4
                color(y, x, yn // 2, xn // 2)
                # 2: 0 ~ 4, 4 ~ 8
                color(y, yn // 2, x + xn // 2, xn)
                # 3: 4 ~ 8, 0 ~ 4
                color(y + yn // 2, yn, x, x + xn // 2)
                # 4: 4 ~ 8, 4 ~ 8
                color(y + yn // 2, yn, x + xn // 2, xn)
    if c == 1:
        blue += 1
    else:
        white += 1
    return

color(0, 0, n, n)
print(white, blue)