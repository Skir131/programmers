def solution(s):
    s_list = list(s)
    answer = sorted(s_list, reverse=True)
    return "".join(answer)