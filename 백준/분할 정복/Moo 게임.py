'''
S(0) = "m o o"
S(1) = "m o o m o o o m o o"
S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"
'''

speak = "m00"

def s(n):
    if n == 0:
        speak
    else:
        return s(n) + s(n - 1)