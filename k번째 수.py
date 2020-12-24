def solution(array, commands):
    answer = []
    for lst in commands:
        ret = array[lst[0]-1:lst[1]]
        ret.sort()
        answer.append(ret[lst[2]-1])
    
    return answer