def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for call in callings:
        idx = rank[call]
        rank[players[idx - 1]] += 1
        rank[call] -= 1
        players[idx], players[idx - 1] = players[idx - 1], players[idx]

    return players