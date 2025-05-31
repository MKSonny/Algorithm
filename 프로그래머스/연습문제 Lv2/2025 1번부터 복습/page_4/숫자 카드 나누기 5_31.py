import math


def solution(arrayA, arrayB):
    answer = 0
    gA = arrayA[0]
    gB = arrayB[0]
    ta = []
    tb = []

    for i in range(len(arrayA)):
        gA = math.gcd(gA, arrayA[i])
        gB = math.gcd(gB, arrayB[i])

    for i in arrayA:
        if i % gB == 0:
            gB = 0
            break

    for i in arrayB:
        if i % gA == 0:
            gA = 0
            break

    return max(gB, gA)