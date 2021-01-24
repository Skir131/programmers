import math

def solution(progresses, speeds):
    work = []
    for i in range(len(progresses)):
        length = math.ceil((100 - progresses[i]) / speeds[i])
        work.append(length)
    print(work)
    stack = []
    result = []
    for w in work:
        count = 0
        while stack and stack[0] < w:
            count += 1
            stack.pop()
        
        if count:
            result.append(count)
        stack.append(w)
       
    result.append(len(stack))
    return result
#1/20 해결