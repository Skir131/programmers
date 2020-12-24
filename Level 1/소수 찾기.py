def solution(n):
    era = [i for i in range(1000001)]
    era[1] = 0
    for i in range(2, 1000001):
        if era[i] == 0:
            continue
        else:
            for j in range(i+i, 1000001, i):
                era[j] = 0          
    answer = 0
    for i in range(1, n+1):
        if era[i] != 0:
            answer += 1
    return answer