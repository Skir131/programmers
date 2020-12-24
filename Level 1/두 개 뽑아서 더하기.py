from itertools import combinations

def solution(numbers):
    answer = []
    #리스트에서 두개씩 뽑기위하여 조합을 이용
    for num_tuple in list(combinations(numbers, 2)):
        #answer에 합이 있다면 패스
        if sum(num_tuple) in answer:
            pass
        #없다면 추가
        else:
            answer.append(sum(num_tuple))
    # 배열을 오름차순으로 정렬하고 이를 반환
    return sorted(answer)