def solution(arr1, arr2):
    #행렬 a by b인 arr1과, c by d인 ar2에 대하여
    #결과 행렬은 a by d이다.
    #문제 조건에 의하여 b == c 이다.
    answer = [ [0 for i in range(len(arr2[0])) ] for j in range(len(arr1))]

    for i in range(len(answer)):
        for j in range(len(answer[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer
# 12/30 해결(2주차 풀이 링크2)