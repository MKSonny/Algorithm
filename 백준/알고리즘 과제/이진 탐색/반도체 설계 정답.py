import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
def binary_search(A, key, low, high):
    if low > high:
        return low
    mid = (low + high) // 2
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search(A, key, low, mid - 1)
    else:
        return binary_search(A, key, mid + 1, high)


# print(res)

# 2, 3, 5


# for i in range(1, len(a)):
#     # 오름차순으로 추가된다.
#     if res[-1] < a[i]:
#         res.append(a[i])
#     #
#     # 2부터 시작했다면 6들어가고 3이 들어가는 순간 다시 초기화된다.
#     # 근데 2는 없어지면 안된다.
#     # 일단 진행
'''
    [4 2 6 3 1 5]에서 작은 값이 들어오면 초기화 해야한다.
    2부터 시작했다면 6들어가고 3이 들어가는 순간 다시 초기화된다.
    2는 살려두고 다음 3을 추가할 방법? 2와 3을 비교해야 한다.
    binary search의 역할? 만약 [2, 6]에서 3을 찾으라고 하면 1을 반환한다.
    만약 [2, 6]에서 1을 찾으라고 한다면 0을 반환한다.
    이 점을 활용해 3을 1위치에 대입한다. 즉 binary search 가 반환하는 값을
    res의 인덱스에 대입한 후 해당 인덱스에 a[i]를 대입한다.
    그리고 다음 숫자는 1이 오는데 여기서 문제가 생긴다.
    1은 2보다 작기 때문에 binary search 는 0을 반환하고 
    res 는 [2, 3]에서 [1, 3]이 된다.
    이후 반복이 모두 종료되면 [1, 3, 5]가 되어 정답 3과 맞고
    제출을 했는데 정답으로 표시됬다. 이해가 안됬다. 하지만 자세히 생각해보니
    2의 위치에 1이 들어가도 상관이 없을 것 같다는 생각이 들었다.
    이유는 2와 1모두 3보다는 작다.
    만약 [1, 3, 5, 2] 이 있다면 가장 길게 증가하는 수는 [1, 3, 5]이다.
    코딩으로 이를 계산하려면 1부터 시작하면 [1, 3, 5], 2는 binary search 이후 1을 반환한다.
    그러면 [1, 2, 5]가 된다. binary search는 절대로 res의 길이보다 큰 숫자를 반환하지 않는다.
    따라서 내부에 자신이 끼어 들어갈 수 있는 인덱스를 반환한다.
'''
    # else:

# 이렇게 하면 -60에 대한 것 밖에 못한다.
max_len = 0
temp = []
temp_calc = []

res = [a[0]]
temp_calc = [(a[0], 0)]

for i in range(1, n):
    # print(i, res[-1], a[i])
    if res[-1] < a[i]:
        res.append(a[i])
        temp_calc.append((a[i], i))
    else:
        idx = binary_search(res, a[i], 0, len(res) - 1)
        res[idx] = a[i]
        temp_calc.append((a[i], idx))

print(temp_calc)
lis_length = len(temp_calc)-1
lis = []

while temp_calc:
    num, idx = temp_calc.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])
# (-60, 0), (-41, 1), (-100, 0), (8, 3), (-8, 2), (-52, 1), (-62, 1), (-76, 1), (-52, 1), (14, 10),
# (-11, 1), (-2, 1), (-54, 1), (46, 14)

'''
7
-100 -62 -61 -52 -11 -2 46 
'''