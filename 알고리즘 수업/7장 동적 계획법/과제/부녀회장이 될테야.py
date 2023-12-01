T = int(input())
for _ in range(T):
    n = int(input())
    m = int(input())

    # 만약 2와 3이 차례대로 입력된다면
    # 3행 3열 2차원 배열을 생성한다.
    # 이는 3행은 1, 2, 3호를 나타내고 3열은 문제의 조건에서 0층부터 시작했으므로 총 3층의 배열을 생성한다.
    apart = [[0 for _ in range(m)] for _ in range(n + 1)]


    for i in range(n + 1):
        for j in range(m):
            if i == 0:
                # 만약 0 층이면 이전 호수의 + 1명 만큼 더한다.
                apart[i][j] = j + 1
            # 이외 2 층이면
            # 현재 살려고 하는 만약 2층 2호에서 살려면
            # 1층 1 ~ 2호를 모두 더한 수의 사람들을 데려와 살아야한다.
            # 이를 나타내는 apart[i - 1][:j + 1]
            # i - 1 -> 이 전층
            # [:j + 1] -> 0 부터 현재 층의 호수까지 합한 값을 저장한다.
            # 해당 과정을 입력 받은 n층, m - 1호까지 입력까지 반복하고
            # 본인의 위치를 반환한다.
            else:
                apart[i][j] = sum(apart[i - 1][:j + 1])

    print(apart[n][m - 1])