def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def gcd_list(arr):
    res = arr[0]
    for i in arr[1:]:
        res = res * i / gcd(res, i)
    return res 

def solution(arr):
    answer = gcd_list(arr)
    return answer
# 1/8 해결(3주차 풀이 링크1)