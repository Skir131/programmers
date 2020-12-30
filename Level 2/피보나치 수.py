def solution(n):
    answer = 0
    fibo = [i for i in range(100001)]
    for i in range(2, 100001):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n] % 1234567
#12/27 해결