import sys

p, m = map(int, sys.stdin.readline().split())
room = []
waiting = []
players = []

for _ in range(p):
    level, name = sys.stdin.readline().rstrip().split()
    players.append((level, name))

while players:
    level, name = players.pop(0)
    level = int(level)
    if len(room) == 0:
        base_level = level

    if level <= base_level + 10 and level >= base_level - 10:
        room.append((level, name))
    else:
        waiting.append((level, name))

    if len(waiting) == m:
        print("Started!")
        for i in waiting:
            print(i[0], i[1])

        waiting.clear()

    if len(room) == m:
        print("Started!")
        for i in room:
            print(i[0], i[1])

        room.clear()

        if len(waiting) > 0:
            level, name = waiting.pop(0)
            base_level = level
            room.append((level, name))

            while waiting:
                players.insert(0, waiting.pop(0))

while room:
    level, name = room.pop(0)
    print("Waiting!")
    print(level, name)