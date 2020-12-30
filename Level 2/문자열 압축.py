def solution(s):
    answer = []
    for length in range(1, len(s)+1):
        count = 1
        al = s[:length]
        result = ""
        for i in range(length, len(s), length):
            if al != s[i:i+length]:
                if count != 1:
                    result += str(count) + al
                else:
                    result += al
                al = s[i:i+length]
                count = 1
            else:
                count += 1
        if count != 1:
            result += str(count) + al
        else:
            result += al          
        answer.append(result)
        
    answer = [len(ans) for ans in answer]
    return min(answer)
# 12/30 해결