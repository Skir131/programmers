def solution(priorities, location):
    answer = 0
    #우선 순위를 판별하기 위한 list를 생성한다.
    maximum_list = sorted(priorities, reverse=True)
    #우선 순위에 대한 원소를 가져오기 위한 인덱스값을 만든다.
    maximum_idx = 0
    #프린트의 파일을 탐색할 인덱스값을 만든다.
    i = 0
    while True:
        is_print = False
        #프린터를 탐색하면서 주어진 파일에 대한 우선순위가 현재 우선순위와 같다면 이 파일을 프린트 해야한다.
        if priorities[i] == maximum_list[maximum_idx]:
            #프린트를 진행하였으므로 탐색해야할 다음 우선순위를 찾기 위하여 우선 순위에 대한 인덱스 값을 1 더한다.
            is_print = True
            maximum_idx += 1
            #프린트를 진행하였으므로 진행한 횟수를 알리는 answer 값에 1 더한다.
            answer += 1
        
        #만약, 프린트를 했는데 이 파일의 인덱스값이 반환해야 할 location의 인덱스와 같다면, 그 answer값을 return한다.
        if is_print:
            if i == location:
                return answer
        i += 1
        i = i % len(priorities)
        maximum_idx = maximum_idx % len(maximum_list)
#12/25 해결(1주차 풀이 링크5)