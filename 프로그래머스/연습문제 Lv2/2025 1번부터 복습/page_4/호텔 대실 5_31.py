from collections import deque


def solution(book_time):
    answer = 0

    s = []
    book_time.sort()

    book_time = deque(book_time)

    def calc(a):
        s = []
        for i in a:
            a, b = map(int, i.split(':'))
            s.append(a * 60 + b)

        return s

    for i in range(len(book_time)):
        book_time[i] = calc(book_time[i])

    rooms = [[] for _ in range(1000)]

    while book_time:
        t = book_time.popleft()

        for i in range(1000):
            if len(rooms[i]) > 0 and rooms[i][-1][1] + 10 <= t[0]:
                rooms[i].append(t)
                break
            elif len(rooms[i]) == 0:
                rooms[i].append(t)
                break

    for i in rooms:
        if len(i) > 0:
            answer += 1

    return answer