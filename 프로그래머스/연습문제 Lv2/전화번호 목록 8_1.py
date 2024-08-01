def solution(phone_book):
    answer = True

    hash_map = set(phone_book)

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num
            if arr in hash_map and arr != nums:
                return False

    return True