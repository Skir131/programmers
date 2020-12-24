def solution(a, b):
    day_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    today = 5
    for i in range(1, a):
        today += month_list[i-1]
    today += b-1   
    today %= 7
    
    answer = day_list[today]
    return answer