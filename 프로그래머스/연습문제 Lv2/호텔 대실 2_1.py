from collections import deque


def solution(book_time):
    answer = 0

    book_time.sort()

    room = []

    book_time = deque(book_time)

    t = book_time.popleft()

    room.append([t])

    def check_time(t):
        s_hour, s_minute = t.split(':')

        return int(s_hour) * 60 + int(s_minute)

    print()

    while book_time:

        s = book_time.popleft()

        flag = False
        for tr in room:
            if int(check_time(s[0])) >= int(check_time(tr[-1][-1])) + 10:
                tr.append(s)
                flag = True
                break

        if not flag:
            room.append([s])
            # break

    return len(room)