def solution(n, lost, reserve):
    reserve_2 = list(set(reserve)-set(lost))
    lost_2 = list(set(lost)-set(reserve))
    answer = n - len(lost_2)
    for s in reserve_2:
        if not lost_2:
            break
            
        if s-1 in lost_2:
            answer += 1
            lost_2.remove(s-1)
        elif s+1 in lost_2:
            answer += 1
            lost_2.remove(s+1)
        else:
            continue

    return answer