from math import gcd
from functools import reduce


def solution(arrayA, arrayB):
    answer = 0

    def calculate_gcd(array):
        return reduce(gcd, array)

    a = calculate_gcd(arrayA)
    b = calculate_gcd(arrayB)

    def check(idx1, idx2, arr1, arr2):
        for i in range(len(arr1)):
            if arr2[i] % idx1 == 0:
                idx1 = 0
                break

        for i in range(len(arr1)):
            if arr1[i] % idx2 == 0:
                idx2 = 0
                break

        return max(idx1, idx2)

    return check(a, b, arrayA, arrayB)

    # return answer