def solution(nums):
    answer = 0

    n = len(nums) // 2

    set_nums = set(nums)

    if len(set_nums) < n:
        return len(set_nums)
    else:
        return n