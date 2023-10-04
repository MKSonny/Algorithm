n = int(input())
movie = 666
cnt = 0

# n = 3
while True:
    # 1666
    # 2666
    if '666' in str(movie):
        # cnt = 1
        # cnt = 2
        # cnt = 3
        cnt += 1
        if cnt == n:
            print(movie)
            break
    # 667
    # 1667
    movie += 1