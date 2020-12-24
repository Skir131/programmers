from collections import defaultdict

def solution(participant, completion):
    #효율성 테스트 통과를 위하여 해싱이 있는 딕셔너리를 사용
    dict = defaultdict(int)
    #defaultdict로 하고, 이름이 명시될 때마다 +=1 
    for val in participant:
        dict[val] += 1
    for player in completion:
        #completion에서 나온 이름을 key로 했을 때, 이에 해당하는 value의 값을 -=1 
        #이때 0이라면 더이상 호출되지 않으므로 제거한다.
        #제거함으로써 마지막에 남은 이름은 한명이 된다.
        dict[player] -= 1
        if dict[player] == 0:
            del dict[player]
            
    return list(dict)[0]