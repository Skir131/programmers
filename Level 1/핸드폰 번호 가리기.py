def solution(phone_number):
    # 길이에서 마지막 4개는 그대로, 그 앞부분은 *이다.
    # phone_number의 길이 n에 대하여 앞 n-4는 *로, 4는 번호 그대로 슬라이싱한다.
    n = len(phone_number)
    answer = "*" * (n-4) + phone_number[-4:]
    return answer
# 1/11 해결(4주차 풀이 링크3)
