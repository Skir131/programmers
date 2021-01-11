def solution(N, stages):
    # players : 각 스테이지를 도달한 사람 수
    # 0 번째 : 1스테이지를 도달한 사람 수, len(N) 번째 : 마지막 스테이지 까지 클리어한 사람 수
    players = [0 for i in range(N+1)]
    for i in range(1, N+1):
        players[i-1] = stages.count(i)   
    # 스테이지별 실패율을 담을 딕셔너리
    dic = {}        
    for i in range(N):
        # 1번째 스테이지의 실패율 : players[i-1]을 전체 사람 수(len(stages)-players[i-1])로 나눈 값
        if len(stages)-sum(players[:i]) == 0:
            dic[i+1] = 0
        else:
            dic[i+1] = players[i] / (len(stages)-sum(players[:i]))
    # 실패율(인덱스 1 값)을 기준으로 sorting, stable sorting이므로 x[1]이 같다면 위치 변경 x
    print(dic)
    miss_rate = list(dic.items())
    miss_rate.sort(key = lambda x : x[1], reverse=True)
    answer = []
    for i in miss_rate:
        answer.append(i[0])
    
    return answer
# 1/11 해결