def solution(s):
    answer = [0,0]
    while True:
        if s == "1":
            return answer

        answer[0] += 1
        answer[1] += s.count("0")
        s_len = s.count("1")
        s = bin(s_len)[2:]
        
    return answer

# 1/11 해결