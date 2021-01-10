def plus_minus_multi(a):
    i = 0
    result = []
    # + - *로 이루어져있는데 +를 1로, -를 2로, *을 3으로 표현.
    sequence = [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
    for sqe in sequence:
        # shallow copy를 방지하기 위하여 list comprehension으로 temp list 생성
        temp = [i for i in a]
        # 우선 순위에 따라서 더하기 빼기 곱하기 진행
        for s in sqe:
            if s == 1:
                plus(temp)
            elif s == 2:
                minus(temp)
            else:
                multi(temp)
        # 연산이 이루어지면 temp list의 길이는 1이다. 그 값을 절댓값으로 저장
        result.append(abs(temp[0]))
    return result

def plus(a):
    i = 1
    while i < len(a):
        if a[i] == "+":
            a[i-1:i+2] = [a[i-1] + a[i+1]]
        else:
            i += 2

def minus(a):
    i = 1
    while i < len(a):
        if a[i] == "-":
            a[i-1:i+2] = [a[i-1] - a[i+1]]
        else:
            i += 2

def multi(a):
    i = 1
    while i < len(a):
        if a[i] == "*":
            a[i-1:i+2] = [a[i-1] * a[i+1]]
        else:
            i += 2
    
def solution(expression):
    a = []
    num = ''
    # operator와 operand를 구별하기 위한 작업
    for i in expression:
        if i.isdigit():
            num += i
        else:
            a.append(int(num))
            a.append(i)
            num = ''
    a.append(int(num))

    result = plus_minus_multi(a)
    return max(result)

#1/4 해결(3주차 풀이 링크2)