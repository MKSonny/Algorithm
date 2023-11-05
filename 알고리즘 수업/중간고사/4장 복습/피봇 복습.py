# 피봇을 기준으로 왼쪽은 피봇보다 작은거 오른쪽은 피봇보다 큰 거
nums = [5, 3, 8, 4, 9, 1, 6, 2, 7]
def pivot_sort(nums, left, right):
    pivot = nums[left]
    low = left + 1
    mid = right // 2
    high = right
    # 아래 조건을 모두 만족해야 while문을 빠져나온다.
    # low는 한차례 감소를 하고 while문을 만나기 때문에
    # low에는 mid 보다 작은 값이 저장되고 while문을 빠져나온다.
    while low <= mid and high >= mid + 1:
        while nums[low] < pivot: low += 1
        while nums[high] > pivot:
            high -= 1
            # 여기서 high는 5보다 작아지면 안된다.
            print('high', high)
        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
    if low > high:
        nums[high], nums[left] = nums[left], nums[high]

pivot_sort(nums, 0, len(nums) - 1)
print(nums)