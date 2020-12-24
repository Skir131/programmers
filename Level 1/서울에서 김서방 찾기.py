def solution(seoul):
    idx = 0
    for i, name in enumerate(seoul):
        if name == "Kim":
            idx = i
    answer = "김서방은 %d에 있다" %idx
    return answer