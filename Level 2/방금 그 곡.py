def return_time(a,b):
    a_list= list(map(int, a.split(":")))
    a_time = a_list[0] * 60 + a_list[1]
    b_list = list(map(int, b.split(":")))
    b_time = b_list[0] * 60 + b_list[1]
    return (b_time - a_time) % 1440

def convert_song(songs):
    # 문자열을 스플릿 또는 인덱싱 하는 과정에서 "#"가 포함되어 있는 코드는 불편하므로,
    # "#"가 포함되어 있는 코드를 소문자로 변경한다.
    while True:
        if songs.find("C#") == -1:
            break
        else:
            songs = songs.replace("C#", "c")           
    while True:
        if songs.find("D#") == -1:
            break
        else:
            songs = songs.replace("D#", "d")
    while True:
        if songs.find("E#") == -1:
            break
        else:
            songs = songs.replace("E#", "e")
    while True:
        if songs.find("F#") == -1:
            break
        else:
            songs = songs.replace("F#", "f")
    while True:
        if songs.find("G#") == -1:
            break
        else:
            songs = songs.replace("G#", "g")
    while True:
        if songs.find("A#") == -1:
            break
        else:
            songs = songs.replace("A#", "a")
            
    return songs

def is_melody_of_song(melodies, songs):
    # melodies : melody str, songs : song str
    # kmp법을 이용하여 songs안에 melodies가 있는지 판단한다.
    pat = melodies
    txt = songs
            
    # KMP
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1

def solution(m, musicinfos):
    m = convert_song(m)
    lists = [] 
    # 먼저 문자열을 리스트로 변경하여 계산하기 쉽게 변경한다.
    # lists의 원소 : (재생 길이, 노래 제목, 재생된 총 악보)
    for string in musicinfos:
        lst = string.split(",")
        #시작한 시각, 끝난 시간을 기준으로 총 몇분간 곡이 재생되어있는지 계산한다.
        time = return_time(lst[0], lst[1])
        lst[:2] = [time]
        
        #곡의 코드를 변환한다.(#를 제거하기 위함)
        lst[2] = convert_song(lst[2])

        #곡의 시각을 기준으로 코드의 길이를 늘려야 한다.
        #예를 들어, 곡의 코드가 "ABC"일 때, 곡이 두 번 이상 재생된 경우
        #네오는 "CBA"를 들을 수 있다. 따라서 "ABC"를 늘려서 "BCA"를 찾을 수 있도록 늘려야한다.
        q,r = divmod(time, len(lst[2]))
        lst[2] = lst[2] * q + lst[2][:r]
        lists.append(lst)
    
    answer = []
    #노래 안에 네오가 들은 멜로디가 있는지 찾는다.
    for song in lists:
        #kmp법은 문자열을 못찾으면 -1이다.
        if is_melody_of_song(m, song[2]) == -1:
            continue
        else:
            answer.append([song[0], song[1]])

    # 찾은 노래가 없다면 길이가 0이므로 "(None)"을 반환
    if len(answer) == 0:
        return "(None)"
    # 조건에 따르면, 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 
    # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다. 
    # 따라서 kmp으로 문자열을 찾을 때 time을 넣어서 time을 기준으로 정렬하고 첫 번째 노래를 반환한다.
    else:
        answer.sort(key = lambda x : x[0], reverse=True)
        return answer[0][1]
# 1/21 해결(5주차 풀이 링크4)