def solution(s):
    answer = []
    #길이를 1부터 len(s)까지 반복한다.
    for length in range(1, len(s)+1):
        # 먼저 첫번째 pasring된 문자열로 시작한다.
        count = 1
        al = s[:length]
        result = ""
        # 두 번째 pasring된 문자열부터 끝까지 반복한다.
        # 파이썬의 인덱스 슬라이싱은 end 범위가 길이 이상으로 늘어나도 알아서 조절해서 슬라이싱 해주기 때문에,
        # 두 번째부터 마지막까지 계속 반복한다.
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
        # 마지막 pasring된 문자열만 따로 계산한다.
        if count != 1:
            result += str(count) + al
        else:
            result += al          
        answer.append(result)
        
    answer = [len(ans) for ans in answer]
    return min(answer)
# 12/30 해결(2주차 풀이 링크1)