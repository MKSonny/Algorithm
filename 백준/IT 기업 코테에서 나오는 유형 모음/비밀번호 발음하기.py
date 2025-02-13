import sys

vowels = set(['a', 'e', 'i', 'o', 'u'])

def is_vowels(charactor):
    if charactor in vowels:
        return 1
    else:
        return 0


def is_safe(password):
    first, second, third = 0, 1, 1
    prev = password.pop(0)
    vowel_cnt = 0

    if prev in vowels and first == 0:
        first = 1

    while password:
        charactor = password.pop(0)
        if charactor in vowels and first == 0:
            first = 1
        if is_vowels(prev) == is_vowels(charactor):
            vowel_cnt += 1
            if vowel_cnt == 2:
                second = 0
        else:
            vowel_cnt = 0
        if prev == charactor:
            if charactor == 'e' or charactor == 'o':
                third = 1
            else:
                third = 0
        prev = charactor

    if first * second * third == 1:
        return True
    else:
        return False


while True:
    string = sys.stdin.readline().rstrip()
    if string == 'end':
        break
    password = list(string)

    if is_safe(password):
        print("<" + string + "> is acceptable.")
    else:
        print("<" + string + "> is not acceptable.")