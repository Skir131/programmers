def solution(n, words):
    answer = []
    num = 0
    prev = ''
    # words에 있는 단어를 하나씩 추출
    for word in words:
        #번호 차례를 반환하기 위한 num
        num += 1
        #시작인 경우
        if not prev:
            prev = word
            answer.append(prev)
            continue
        # 중복된 단어인 경우        
        elif word in answer:
            a = num % n
            if a == 0:
                a = n
            if not num / n == int(num / n):
                b = num // n + 1
            else:
                b = num // n
            return [a, b]
        # 끝말잇기가 성립한 경우              
        elif prev[-1] == word[0]:
            prev = word
            answer.append(prev)
        # 끝말잇기에 실패한 경우
        else: 
            a = num % n
            if a == 0:
                a = n
            if not num / n == int(num / n):
                b = num // n + 1
            else:
                b = num // n
            return [a, b]
        # round는 사사오입때문에 쓸 수가 없다.
        # [번호, 차례]에서, 번호 : 1 2 3 4 5 6 7 8 9 를 1 2 3 1 2 3 1 2 3 으로 바꿔야 한다.
        # num % n 을 하면 3 6 9가 0이 되는데 0이 될 경우 3으로 되게 한다.
        # 차례 : 1 2 3 4 5 6 7 8 9이 1 1 1 2 2 2 3 3 3이 되어야 한다.
        # num % n이 0이 아닌 경우 즉, 1 2는 1 1이 되어야 하고,
        # 4 5 는 2가 되어야 한다. 즉, num % n 인 경우는 제외, 나머지는 num // n + 1을 한다.
        

    return [0,0]

# 1/11 해결 (3주차 풀이 링크5)