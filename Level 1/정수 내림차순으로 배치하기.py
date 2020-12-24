def solution(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n = n // 10
    answer.sort(reverse = True)
    answer = list(map(str, answer))
    return int("".join(answer))