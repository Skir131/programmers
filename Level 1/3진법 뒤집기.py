def conv(n, k):
    if not n:
        return ""
    base = [0,1,2]
    return str(base[n%k]) + conv(n//k, k)

def solution(n):
    a = conv(n, 3)
    answer = int(a, 3)  
    return answer