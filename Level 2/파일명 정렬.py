def solution(files):
    
    file_list = []
    answer = []
            
    for file in files:
        ret = []
        num = ""
        idx = 0
        #숫자가 시작하는 지점 전이 HEAD의 마지막이다.
        while True:
            if file[idx].isdigit():
                break
            else:
                idx += 1
        
        i = idx
        #숫자가 아니게 되는 지점 전이 NUMBER의 마지막이다.
        #그 전까지 num을 계속 저장한다.
        while i < len(file):
            if file[i].isdigit():
                num += file[i]
                i += 1
            else:
                break
        #파일명 전체를 리스트의 첫 번째.
        ret.append(file)
        #HEAD를 리스트의 두 번째. 단 정렬을 할 때 대소문자를 구별하지 않으므로 소문자로 변경해서 저장.
        ret.append(file[:idx].lower())
        #NUMBER을 리스트의 세 번째로 저장.
        ret.append(int(num))
        file_list.append(ret)
    
    #전체 리스트를 정렬하되, HEAD를 처음으로 NUMBER을 그 다음을 기준으로 정렬한다.
    file_list.sort(key = lambda x: (x[1], x[2]))
    for x in file_list:
        answer.append(x[0])
           
    return answer
# 12/30 해결(2주차 풀이 링크3)