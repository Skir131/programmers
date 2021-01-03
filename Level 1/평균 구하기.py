from functools import reduce
def solution(arr):
    # reduce 기능을 이용하여 해결
    return reduce(lambda x,y: x + y, arr, 0) / len(arr)

# 1/4 해결