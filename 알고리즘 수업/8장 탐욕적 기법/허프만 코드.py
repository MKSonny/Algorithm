import heapq
'''
힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해
고안된 완전이진트리를 기본으로 한다. 

힙 property : A가 B의 부모노드이면 A의 키값과 B의 키값 사이에는 대소 관계가 성립한다

최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙
'''
def make_heap_tree(freq, label):
    n = len(freq)
    h = []

    for i in range(n):
        # freq[i]를 기준으로 정렬된다.
        # label[i]: 문자열이 더 길수록 뒤로 정렬되게 하기 위해
        heapq.heappush(h, (freq[i], label[i]))

    # range(1, n) 총 n - 1만큼 반복하게 하려고
    for i in range(1, n):
        e1 = heapq.heappop(h)
        e2 = heapq.heappop(h)
        heapq.heappush(h, (e1[0] + e2[0], e1[1] + e2[1]))
        print(e1, "+", e2)

    print(heapq.heappop(h))

label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]
make_heap_tree(freq, label)