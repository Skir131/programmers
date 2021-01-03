from functools import reduce
def solution(arr):
    return reduce(lambda x,y: x + y, arr, 0) / len(arr)

# 1/4 해결