from collections import deque

def solution(people, limit):
    answer = 0

    people.sort()
    people = deque(people)

    while True:
        a = people.pop()
        answer += 1

        if len(people) == 0:
            break

        if len(people) > 0 and a + people[0] <= limit:
            people.popleft()
            if len(people) == 0:
                break

    return answer