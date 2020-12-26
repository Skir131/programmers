def conv(n, k):
    rate = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    if n == 0:
        return ""
    else:
        return conv(n//k, k) + rate[n%k]

def solution(n, t, m, p):
    answer = ""
    game = []
    i = 0
    number = 0
    is_continue = True
    
    while True:
        string = conv(number, n)
        if not string:
            string = "0"
            
        j = 0
        while j < len(string):
            game.append(string[j])
            j += 1
            i += 1
            
            if i == t * m:
                is_continue = False
                break
                
        if is_continue == False:
            break
        else:
            number += 1

    result = [ ["" for i in range(m)] for j in range(t)]
    i = 0
    for x in range(t):
        for y in range(m):
            result[x][y] = game[i]
            i += 1
    
    for x in range(t):
        answer += result[x][p-1]
        
    return answer
# 12/26 해결