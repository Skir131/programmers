def solution(number, k):
    #처음에 스택에 한개를 추가
    stack = [number[0]]
    for num in number[1:]:
        # num에 대해서,
        # 1. stack에 원소가 남아있을 때 까지 반복한다. 149에 대해서 9가 맨 앞을 와야 하므로 1,4를 없앤다.
        # 2. k > 0 : k는 지워야할 수 인데, k = 0이면 더이상 지울 필요가 없다.
        # 3. stack[-1] < num : 스택의 마지막 값에 대해서, 4 9 이면 4를 지우고, 9 4이면 지우지 않는다.
        while len(stack) > 0 and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        # 4. num을 스택에 append한다.
        stack.append(num)

    # k = 0이 아니라면, 즉 지워야 할 수가 남아있다면 그 만큼 마지막 수를 지운다.
    # 끝을 지울 수 있는 이유는 이미 for, while를 통해서 앞의 수는 큰 수로 정렬이 완료되었기 때문이다.
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)
# 1/11 해결 
# 출처 : https://eda-ai-lab.tistory.com/465?category=766271
