def solution(priorities, location):
    answer = 0
    maximum_list = sorted(priorities, reverse=True)
    maximum_idx = 0
    i = 0
    while True:
        is_print = False
        if priorities[i] == maximum_list[maximum_idx]:
            is_print = True
            maximum_idx += 1
            answer += 1
        
        if is_print:
            if i == location:
                return answer
        i += 1
        i = i % len(priorities)
        maximum_idx = maximum_idx % len(maximum_list)
