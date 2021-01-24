def convert(n):
    # 124는 3진법이다. 하지만 앞 자리가 바뀌는 기준은 4, 7, 10 이므로 이를 나눌 수 있게 하기 위하여
    # n-1을 3으로 나눈다.
    q, r = divmod(n-1, 3)

    # q가 0이라면 즉, 1,2,3이라면 나머지는 0,1,2이다 이를 각각 1,2,4로 반환한다.
    # 이는 q가 0이 아닌 경우에 대해서 종료조건으로 사용한다.
    if q == 0:
        return "124"[r]
    # 4라면 q=1,r=0 => q=1은 q=0 r=0이 되어 1을 반환한다. => 결과는 11
    # 8이라면 q=2,r=1 => q=2는 q=0 r=1이 되어 2를 반환한다. => 결과는 21
    # 10이라면 q=3,r=0 => q=3은 q=0 r=2이 되어 4를 반환한다. => 결과는 41
    else:     
        return convert(q) + "124"[r]

def solution(n):
    return convert(n)

# 1/20 해결(5주차 풀이 링크5)
# 참고 출처 : https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-124-%EB%82%98%EB%9D%BC%EC%9D%98-%EC%88%AB%EC%9E%90-in-python