def solution(bandage, health, attacks):
    answer = 0
    o_health = health
    cnt = 0

    for i in range(1, 1000 + 1):
        if health > o_health:
            health = o_health

        if i == attacks[0][0]:
            t, d = attacks.pop(0)
            health -= d
            cnt = 0
            if health <= 0:
                return -1
            if len(attacks) == 0:
                return health
            continue

        if health < o_health:
            cnt += 1
            if cnt >= bandage[0]:
                health += bandage[2]
                cnt = 0
            health += bandage[1]

    return health