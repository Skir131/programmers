import collections

def truck_sum(stack):
    sum = 0
    for v in stack:
        sum += v[0]
    return sum

def solution(bridge_length, weight, truck_weights):
    # 튜플로 담기 (kg, duration)
    stack = collections.deque()
    
    time = 0
    truck = 0
    while truck != len(truck_weights) or stack:
        #print("시작", stack, time)
        time += 1
        if stack:
            while stack:
                if stack[0][1] == bridge_length:
                    stack.popleft()
                else:
                    break
                    
        if truck < len(truck_weights) and truck_sum(stack) + truck_weights[truck] <= weight:
            stack.append([truck_weights[truck], 0])
            truck += 1
            
        for v in stack:
            v[1] += 1
        #print("끝", stack)
    return time
# 1/20 해결