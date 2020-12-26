from functools import reduce
from itertools import permutations, combinations

def solution(numbers):
    #에라토스테네스의 체를 이용하여 소수를 판별한다.
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
    #다음과 같은 방식을 이용해 lst에 numbers의 부분집합을 추가한다.
    for i in range(len(numbers)+1):
        c = combinations(list(numbers), i)
        lst.extend(c)
        
    for l in lst:
        if not l:
            continue
        #numbers가 17일때 뽑을 수 있는 방법은 1, 7, 17인데 이 17의 경우 17도 되지만 71도 된다.
        #따라서 permutation을 진행하여 두가지 케이스를 모든 만들어주고, 각 경우에 대해서 소수를 판별한다.
        l = list(permutations(l, len(l)))
        for number in l:
            number = int("".join(number))
            if era[number] == 0:
                continue
            elif era[number] in check_answer:
                continue
            else:
                #"022"의 경우 2에 대해서 이미 소수를 만들었으므로 2에 대해서 재추가를 할 수 없다.
                #임의의 list를 만들고 소수를 만들었다면 이 list에 넣고 중복을 방지한다. 
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