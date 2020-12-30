def solution(s):
    answer = ''
    lst = s.split(" ")
    lst = sorted(list(map(int, lst)))
    answer = str(lst[0]) + " " + str(lst[-1])
    return answer
# 12/27 해결