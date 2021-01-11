def solution(x, n):
    answer = []
    #초항을 x로, 공차를 x로 하는 n개의 수열을 반환한다.
    for i in range(1,n+1):
        answer.append(x*i)
    return answer
# 1/11 해결(4주차 풀이 링크4)