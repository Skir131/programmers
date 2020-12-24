from functools import reduce

def solution(arr, divisor):
    answer = []
    answer = reduce(lambda x, y: x + [y] if y % divisor == 0 else x, arr, [])
    if not answer:
        return [-1]
    return sorted(answer)