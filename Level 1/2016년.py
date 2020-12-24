def solution(a, b):
    day_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    today = 5
    #5월이면 4월까지의 일수를 더한다.
    for i in range(1, a):
        today += month_list[i-1]
    #1월 2일이라면 하루를 더한다. 즉, b일에 대해서 b-1만큼 더한다.
    today += b-1   
    today %= 7
    
    answer = day_list[today]
    return answer