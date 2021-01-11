def solution(n, arr1, arr2):
    answer = []
    map = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        num = str(bin(arr1[i])[2:])
        num = "0" * (n-len(num)) + num
        for j in range(len(num)):
            if num[j] == "0":
                continue
            else:
                map[i][j] = 1
    for i in range(n):
        num = str(bin(arr2[i])[2:])
        num = "0" * (n-len(num)) + num
        for j in range(len(num)):
            if num[j] == "0":
                continue
            else:
                map[i][j] = 1
    for i in range(n):
        string = ''
        for j in range(n):
            if map[i][j] == 1:
                string += "#"
            else:
                string += " "
        answer.append(string)
    
    return answer
# 1/11 해결