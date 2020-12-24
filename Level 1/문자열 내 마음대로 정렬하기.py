def solution(strings, n):
    x = sorted(strings, key = lambda x : x[n])
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j][n] == x[j+1][n]:
                if x[j] > x[j+1]:
                    x[j], x[j+1] = x[j+1], x[j]
    
    return x