def solution(edges):
    answer = []

    find = {}

    for s, e in edges:
        if not find.get(s):
            find[s] = [0, 0]
        if not find.get(e):
            find[e] = [0, 0]

        find[s][0] += 1
        find[e][1] += 1

    answer = [0, 0, 0, 0]

    for i in find:
        if find[i][0] == 0 and find[i][1] >= 1:
            answer[2] += 1
        elif find[i][0] >= 2 and find[i][1] >= 2:
            answer[3] += 1
        elif find[i][0] >= 2 and find[i][1] == 0:
            answer[0] = i

    answer[1] = find[answer[0]][0] - (answer[2] + answer[3])
    # 생성된 지점에서 나가는 간선이 2개인데 막대 그래프가 1개 나온다면,
    # 반드시 나가는 간선 1개는 다른 그래프를 형성해야하는데 팔자 그래프도 없다고 한다면
    # 반드시 도넛 그래프다.
    return answer