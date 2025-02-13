import sys

p, m = map(int, sys.stdin.readline().split())
rooms = [[] for _ in range(p)]
waiting = []
players = []

for _ in range(p):
    level, name = sys.stdin.readline().rstrip().split()
    level = int(level)

    for room in rooms:
        if len(room) == m:
            continue
        if len(room) == 0:
            room.append((level, name, level))
            break
        elif room[0][2] - 10 <= level <= room[0][2] + 10:
            room.append((level, name))
            break

def print_room(room):
    room.sort(key=lambda o: o[1])
    for i in room:
        print(i[0], i[1])


for room in rooms:
    if len(room) == m:
        print("Started!")
        print_room(room)
    elif len(room) > 0:
        print("Waiting!")
        print_room(room)