def solution(s):
    count = 0
    #올바른 괄호라는 것은 "("의 개수와 ")"의 개수가 같은 것이다.
    #또한, ")("와 같이 ")"이 "("보다 많을 경우 올바른 괄호가 아니다.
    #이를 판단하기 위해서 "("는 +=1 ")" -= 1을 하여 ")"의 개수가 더 많을 경우 return False,
    #"("가 더 많으면 count > 0 이므로 return count == 0을 하여 0일 때만 True를 반환하도록 한다.
    for i in s:
        if i == "(":
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False

    return count == 0

# 1/21 해결(5주차 풀이 링크2)