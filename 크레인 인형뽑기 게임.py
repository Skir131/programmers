from collections import deque

def solution(board, moves):
    length = len(board)
    box = []
    answer = 0
    for num in moves:
        for idx in range(length):
            if board[idx][num-1] == 0:
                continue
            else:    
                box.append(board[idx][num-1])
                board[idx][num-1] = 0
                break
        if len(box) > 1:
            if box[-1] == box[-2]:
                box.pop()
                box.pop()
                answer += 2
               
    return answer