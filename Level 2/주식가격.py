import collections

def solution(prices):
    deque = []
    result = [0] * len(prices)
    
    for i, cur in enumerate(prices):
        while deque and cur < prices[deque[-1]]:
            last = deque.pop()
            result[last] = i - last 
        deque.append(i)
    
    while deque:
        last = deque.pop()
        result[last] = len(prices) - 1 - last
            
    return result

# 1/20 해결