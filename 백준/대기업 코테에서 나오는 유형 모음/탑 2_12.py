import sys

n = int(sys.stdin.readline())

lo = list(map(int, sys.stdin.readline().split()))

di = {}
for idx, i in enumerate(lo):
    if i not in di.keys():
        di[i] = [idx]
    else:
        di[i].append(idx)

print(di)
keys = di.keys()
to = []

# def find(q, idx):
#     lt = 0
#     rt = idx
#     while lt <= rt:
#         mid = (lt + rt) // 2
#         if idx < mid:
#             lt = mid + 1
#         else:
#             rt = mid - 1
#
#     print(rt)


for idx, i in enumerate(lo):
    q = []
    # print(i, end=' ')
    for k in keys:
        if k > i:
            q.extend(di[k])

    print(q)
    # print()
    # print(q)

# print(to)
# keys = di.keys()
# q = [[] for _ in range(n)]
#
# for idx, i in enumerate(lo):
#     for k in keys:
#         if k >= i:
#             for ko in di[k]:
#                 if ko < idx:
#                     q[idx].append(ko + 1)
#                     # print(i, ko)
#
# an = []
# for qi in q:
#     if len(qi) == 0:
#         an.append(0)
#     else:
#         an.append(max(qi))
#
# print(*an)
# 각 탑의 인덱스를 딕셔너리로 관리
# 6 9 5 7 4 2 1 4 5 1 2 8
# 4보다 큰 숫자들 중 가장 오른 쪽에 있는 곳이면서 4의 인덱스보다
# 작은 곳을 한 번에 찾아야 함
# 이진 탐색 불가?
# 7 보다 크고 9보다 작은 값들 중에서 이진 탐색
# 만약 발견한다면