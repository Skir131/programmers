from itertools import combinations, permutations

def solution(number, k):
    number = list(number)
    i = 0  
    index = 0 
    while i < k:
        if (k-i) == len(number) - index :
            return "".join(number[:index])

        if number[index] < number[index+1]:
            del number[index]
            i += 1
        else:
            index += 1

    return "".join(number)

print(solution("4177252841", 4))