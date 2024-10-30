def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = []
    while truck_weights:
        bridge.append(truck_weights.pop(0))
        while len(bridge) > bridge_length or sum(bridge) > weight:
            bridge = []
            answer += bridge_length
        answer += 1
    if bridge:
        answer += bridge_length

    return answer