import sys
import heapq

# 힙큐와 반복문을 사용해서 최대한 시간복잡도를 낮춰도 시간 초과가 나온다.
# 아래처럼 sys로 input을 받아야 시간 초과가 발생하지 않는다.
n, m = map(int, sys.stdin.readline().split())

dia = []
bag = []


for _ in range(n):
    heapq.heappush(dia, list(map(int, sys.stdin.readline().split())))


for _ in range(m):
    bag.append(int(sys.stdin.readline()))

bag.sort()
# print(dia[-1][1])
# print(bag[0])

# 먼저 가방과 다이아몬드를 무게 순으로 정렬한다.
max_value = 0
temp = []


for weight in bag:
    # bag[0] 가장 작은 가방
    while dia and weight >= dia[0][0]:
        # 가장 가벼운 것의 가치부터 가져온다.
        heapq.heappush(temp, -heapq.heappop(dia)[1])
        # dia_get = dia.pop(0)
        # temp.append(dia_get)
    # temp가 비어있지 않다면
    if temp:
        # 아래 처럼하면 가장 싼 다이아가 나온다.
        # 방지하기 위해 위에서 -를 붙혀 오름차순이 되도록 한다.
        max_value += (-heapq.heappop(temp))

    # dia가 비어있다는 의미는 temp에 모두 넣었다는 것,
    elif not dia:
        break

print(max_value)
'''
    만약 가방이 오름차순이 아닌 내림차순으로 정렬되어 있었다면
    만약 다이아의 무게가 = [1, 10, 100] 이고 (무게와 가치가 동일하다고 가정)
    가방이 [100, 10] 이렇게 되었다면
    temp = [-100, -10, -1] 모두 담고 100의 가치만 더하고 반복은 종료될 것이다.
    그러면 가방 1에 1무게의 다이아를 담는 경우를 처리를 못한다.
    하지만 오름차순으로 정렬했으므로 가방이 [10, 100]
    temp = [-10, -1] 무게 10인 다이아의 가치를 출력, dia 에는 아직 100이 남아 있다.
    따라서 break를 하지않고 다음 for문으로 즉 다음 가방으로 넘어간다.
    '''
    # print('temp', temp)
    # print('bag', bag)
'''
    아래처럼 하면 예제에서는 모두 맞지만 제출시 인덱스 오류가 발생한다.
    이유는 dia.append()를 할 때 기준 dia 리스트는 위에서 sort을 한 것처럼
    무조건 작은 무게순으로 정렬되어 있어야 한다. 하지만 아래처럼하면
    더 가벼운 무게가 뒤로 가 순서가 맞지 않게 된다.
    그러면 큐를 사용해하는데 큐는 sort 함수가 없어서 제출시 
    시간초과가 발생한다. 따라서 힙큐를 사용해야한다.
    하지만 가방은 위와 같은 문제가 발생하지 않아 리스트로 sorting 하면 된다.
'''