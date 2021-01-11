def solution(dartResult):
    scores = []
    num = ''
    answer = 0
    for i in dartResult:
        if i.isdigit():
            num += i
        elif i == '*':
            if len(scores) == 1:
                scores[-1] *= 2
            else:
                scores[-1] *= 2
                scores[-2] *= 2
        elif i == "#":
            scores[-1] *= (-1)
        else:
            if num != '':
                if i == 'S':
                    a = int(num)
                elif i == 'D':
                    a = int(num) ** 2
                elif i == 'T':
                    a = int(num) ** 3
                scores.append(a)
                num = ""

    return sum(scores)
# 1/11 해결