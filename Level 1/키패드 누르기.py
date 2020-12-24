def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    location_index = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
    # star_index is [3,0] and #_index is [3,2]
        
    answer = ''
    L_hand_index = [3,0]
    R_hand_index = [3,2]

    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            L_hand_index = location_index[num]
        elif num in [3,6,9]:
            answer += "R"
            R_hand_index = location_index[num]
        elif num in [2,5,8,0]:
            L_distance = distance(L_hand_index, location_index[num])
            R_distance = distance(R_hand_index, location_index[num])
            if L_distance < R_distance:
                answer += "L"
                L_hand_index = location_index[num]
            elif L_distance > R_distance:
                answer += "R"
                R_hand_index = location_index[num]
            else:
                if hand == "left":
                    answer += "L"
                    L_hand_index = location_index[num]                 
                else:   
                    answer += "R"
                    R_hand_index = location_index[num]        
    return answer