def solution(s):
    answer = []
    for length in range(len(s)):
        i = 0
        count = 0
        al = s[:length]
        result = ""
        while i < len(s):
            print(al)
            if al != s[i:i+length]:
                if count != 1:
                    result += str(count) + al
                else:
                    result += al
                al = s[i:i+length]
                count = 1
            else:
                count += 1
            i += length
        
        if count != 1:
            result += str(count) + al
        else:
            result += al          
        answer.append(result)
        
    print(answer)   
    return len(min(answer))

print(solution("abcabcdede"))