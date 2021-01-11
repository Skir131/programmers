def solution(x):
    #x를 문자열로 바꾸고 리스트로 바꾸면 18에 대해서 ["1", "8"]이 된다.
    #이를 map(int, list)로 하여 [1, 8]로 바꾸고 sum(list) = 9를 만든다.
    #여기서 x % sum(list) == 0이면 True, else False
    a = True if x % sum(list(map(int, list(str(x))))) == 0 else False
    return a
# 1/11 해결(4주차 풀이 링크2)