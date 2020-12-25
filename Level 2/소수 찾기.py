from functools import reduce
from itertools import permutations, combinations

def solution(numbers):
    era = [i for i in range(10000001)]
    era[1] = 0
    for i in range(2, 10000001):
        if era[i] == 0:
            continue
        else:
            for j in range(i+i, 10000001, i):
                era[j] = 0      
    
    answer = 0
    check_answer = []
    lst = []
    for i in range(len(numbers)+1):
        c = combinations(list(numbers), i)
        lst.extend(c)
        
    for l in lst:
        if not l:
            continue
        l = list(permutations(l, len(l)))
        for number in l:
            number = int("".join(number))
            if era[number] == 0:
                continue
            elif era[number] in check_answer:
                continue
            else:
                check_answer.append(era[number])
                answer += 1
    return answer

'''
부분집합 만들기 참고 : https://it-sunny-333.tistory.com/26
'''

'''
원래 한 방식: 
def powerset(lst):
    return reduce(lambda res, x: res + reduce(lambda sub, y: sub + [y+[x]], res, []), lst, [[]])
'''