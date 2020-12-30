def solution(files):
    
    file_list = []
    answer = []
            
    for file in files:
        ret = []
        num = ""
        idx = 0
        while True:
            if file[idx].isdigit():
                break
            else:
                idx += 1
        
        i = idx
        while i < len(file):
            if file[i].isdigit():
                num += file[i]
                i += 1
            else:
                break
        ret.append(file)
        ret.append(file[:idx].lower())
        ret.append(int(num))
        file_list.append(ret)
    
    file_list.sort(key = lambda x: (x[1], x[2]))
    for x in file_list:
        answer.append(x[0])
           
    return answer
# 12/30 해결