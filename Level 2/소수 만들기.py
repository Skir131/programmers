import itertools

def solution(nums):
    answer = -1

    #에라토스테네스의 체를 이용하여 소수를 판단한다.
    era = [i for i in range(3000)]
    era[1] = 0
    for i in range(2, 3000):
        if era[i] == 0:
            continue
        else:
            for j in range(i+i, 3000, i):
                era[j] = 0
    
    #리스트에서 3개를 뽑아오기 위해서 combinations를 이용.
    #뽑아온 3개의 합한 값을 인덱스로 하였을 때, era list의 값이 0이라면
    #소수가 아니고, 0이 아니라면 소수이므로 count += 1
    #after for loop, return count
    count = 0
    for num in itertools.combinations(nums, 3):
        if era[sum(num)] == 0:
            continue
        else:
            count += 1
    return count
# 1/10 해결(3주차 풀이 링크 3)