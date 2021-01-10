def solution(s):
    #스택을 이용
    stack = []
    for i in range(len(s)):
        #스택의 마지막 값과 s[i]가 같다면 스택값은 버리고,
        if stack != [] and stack[-1] == s[i]:
            stack.pop()
        #그렇지 않다면 스택에 값을 추가한다.
        else:
            stack.append(s[i])
    #스택에 값이 남아있으면 짝지어지지 않는 경우이다.
    if not stack:
        return 1
    else:
        return 0
# 1/11 해결(3주차 풀이 링크4)
    