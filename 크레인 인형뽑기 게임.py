from collections import deque

def solution(board, moves):
    length = len(board)
    #인형을 넣을 리스트 생성
    box = []
    answer = 0
    #무브만큼 for loop 진행
    for num in moves:
        for idx in range(length):
            # 0이면 비어있음을 의미하므로 패스
            if board[idx][num-1] == 0:
                continue
            # 그렇지 않다면 그 값을 가져오고 0으로 변경
            else:    
                box.append(board[idx][num-1])
                board[idx][num-1] = 0
                break
        # box의 길이가 2가 넘는다면 사라질 수 있는 가능성 존재
        # -1와 -2의 값이 같다면 연속으로 같은 인형이 배치된 것이므로 제거하고, answer에 2를 더한다.
        if len(box) > 1:
            if box[-1] == box[-2]:
                box.pop()
                box.pop()
                answer += 2
               
    return answer