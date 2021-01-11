def solution(s):
    answer = []
    #먼저 주어진 문자열을 이중 리스트로 만든다.
    for i in s[1:-1]:
        # "{"은 집합의 시작을 의미한다. 이때 담을 리스트와 문자열을 초기화
        if i == "{":
            ret = []
            num = ''
        # i가 숫자라면 그 값을 추가한다.
        elif i.isdigit():
            num += i
        # "}"은 집합의 끝을 의미한다. 이때 값을 추가하고 리스트를 값에 추가. answer list에 ret list를 추가한다.
        elif i == "}":
            ret.append(int(num))
            num = ''
            answer.append(ret)
        #쉼표는 {,}와 같이 집합 안에 존재하는 경우와, {  }, { }와 같이 집합 사이의 존재하는 경우로 나눌 수 있다.
        #1. 집합 안에 존재하는 경우. 이 때 num은 빈 문자열이 아니므로 num을 ret에 추가하고 num을 초기화한다.
        elif i == ",":
            if num != '':
                ret.append(int(num))
                num = ''
        #2. 집합 밖에 존재하는 경우. "}"에서 num을 초기화 하였으므로 else에서 아무런 작업을 하지 않는다.
            else:
                num = ''
    #집합을 튜플로 바꾸기 위해선 먼저, 집합이 작은 순서부터 해결해나가야 한다.            
    answer.sort(key = lambda x : len(x))
    result = []
    for lst in answer:
        for l in lst:
            if l in result: #result list 안에 집합의 원소가 존재하는 경우 패스. 그렇지 않다면 그 값을 추가한다.
                continue
            else:
                result.append(l)
                
    return result
# 1/11 해결(4주차 풀이 링크 5)