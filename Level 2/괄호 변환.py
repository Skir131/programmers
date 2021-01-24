def is_right(p):
    #올바른 괄호인지 판단하는 문제
    #Level 2의 올바른 괄호 문제와 같다.

    #올바른 괄호라는 것은 "("의 개수와 ")"의 개수가 같은 것이다.
    #또한, ")("와 같이 ")"이 "("보다 많을 경우 올바른 괄호가 아니다.
    #이를 판단하기 위해서 "("는 +=1 ")" -= 1을 하여 ")"의 개수가 더 많을 경우 return False,
    #"("가 더 많으면 count > 0 이므로 return count == 0을 하여 0일 때만 True를 반환하도록 한다.

    k = 0
    for i in range(len(p)):
        if p[i] == "(":
            k += 1
        else:
            k -= 1
        if k < 0:
            return False    
    return True

def return_balance_index(p):
    #균형잡힌 괄호일때의 인덱스를 반환하는 함수
    #"("일 때 k +=1 ")"일 때 k -= 1을 한다.
    #만약 k == 0이라면 "("의 개수와 ")"의 개수가 같을 때의 인덱스이므로 이를 반환한다.
    #현재 문제에선 균형잡힐 때의 인덱스가 두 개 이상일 때 다른 행동을 하라고 규정하지 않았으므로,
    #균형잡힌 문자열의 인덱스를 발견했을 때 그 인덱스를 반환한다.
    k = 0
    for i, v in enumerate(p):
        if v == '(':
            k += 1
        else:
            k -= 1
        if k == 0:
            return i
        
def return_reverse_string(p):
    # 4-4의 u의 괄호 방향을 뒤집기 위한 함수
    # "("라면 ")"를 결과에 붙이고, ")"라면 "("를 결과에 붙인다.
    # for loop이 끝난다면 그 결과를 반환한다.
    string = ''
    for s in p:
        if s == '(':
            string += ")"
        else:
            string += "("
    return string

def solution(p):
    # 예외 처리를 통해 문제풀이 속도 향상
    if len(p) == 0:
        return ''
    if is_right(p):
        return p
    
    # 2번 과정을 위하여 먼저 균형잡힌 문자열이 어디인지 파악하기 위하여
    # 함수를 만들고 인덱스를 반환.
    idx = return_balance_index(p)
    # 그 인덱스를 기준으로 w를 u와 v로 나눈다.(문자열 슬라이싱)
    u = p[:idx+1]; v = p[idx+1:]
    
    # is_right는 올바른 괄호 문자열인지 판단하는 함수
    if is_right(u):
        # 3-1
        return u + solution(v)
    #4번 과정
    else:
        #4-1
        string = '('
        #4-2
        string += solution(v)
        #4-3
        string += ")"
        u = u[1:-1]
        #4-4
        string += return_reverse_string(u)
        #4-5
        return string

# 1/21 해결(5주차 풀이 링크3)
