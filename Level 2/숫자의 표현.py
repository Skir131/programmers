def solution(n):
    count = 0
    for i in range(1, n+1):
        k = 1
        # 주어진 문제를 수식으로 변경
        # 단, 나누기 2를 넣으면 부동소수점의 오차가 발생할 수 있기 때문에
        # 비교하려는 대상을 n이 아닌 2n으로 변경한다.
        while (k * k + 2 * i * k - k) <= 2 * n:
            # 2n과 같으면 수식이 가능한 것이므로 count +=1,2n을 넘으면 더이상 i를 시작으로 2n을 만들 수 없으므로
            # while loop을 종료시키고, i를 더한다.
            if (k * k + 2 * i * k - k) == 2 * n:
                count += 1
                break
            else:
                k += 1           
    return count
# 1/21 해결(5주차 풀이 링크1)