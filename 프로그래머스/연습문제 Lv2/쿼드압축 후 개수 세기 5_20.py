t_0 = 0
t_1 = 0

#
def solution(arr):
    answer = []

    def multi(y_start, y_end, x_start, x_end):
        total = 0
        global t_0
        global t_1
        print(y_start, y_end, x_start, x_end)
        s = arr[y_start][x_start]
        flag = True

        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                if s != arr[y][x]:
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            if s == 0:
                t_0 += 1
            else:
                t_1 += 1
            print(t_0, t_1)
            return

        multi(y_start, y_end // 2, x_start, x_end // 2)  # 1
        multi(y_start, y_end // 2, x_end // 2, x_end)
        multi(y_end // 2, y_end, x_start, x_end // 2)
        multi(y_end // 2, y_end, x_end // 2, x_end)

    multi(0, len(arr), 0, len(arr))
    print(t_0, t_1)

    return answer

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])