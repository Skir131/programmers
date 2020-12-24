import math

def solution(n):
    answer = 0
    if int(math.sqrt(n)) == math.sqrt(n):
        return pow(math.sqrt(n) + 1, 2)
    else:
        return -1