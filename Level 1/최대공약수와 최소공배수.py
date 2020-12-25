def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)


def solution(n, m):
    answer = []
    if n  < m :
        n, m = m, n
    res = gcd(n, m)
    return [res, n * m / res]