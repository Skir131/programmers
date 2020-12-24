def solution(n):
    lst = ["수", "박"]
    answer = ''
    idx = 0
    for i in range(n):
        answer += lst[idx]
        idx += 1
        idx = idx % 2
    return answer