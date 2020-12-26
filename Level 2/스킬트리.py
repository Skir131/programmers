from itertools import combinations

def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        is_skill = True
        #한 개의 스킬트리에 대해 스트링(이하 string이라 하자.)을 for loop으로 확인한다.
        for i, s in enumerate(skills):
            #이 때, 문자열 s가 skill에 포함되지 않는다면 스킬트리에 영향을 주지 않는 것이다.
            if not s in skill:
                continue
            else:
                # skill : CBD, skill Trees : BACDE에서, s를 B라고 하자.
                # 이때 skill에서 B의 인덱스를 찾고 그 앞부분만을 slicing한 것을 ret이라고 했을 때,
                # string에서 s 앞 부분에 ret에 대한 모든 것이 있어야 한다. 
                ret = skill[:skill.index(s)]
                count = 0
                for check_skill in ret:
                    if check_skill in skills[:i]:
                        count += 1
                    else:
                        continue
                #앞선 예를 반복하면, string의 B앞엔 아무것도 없으므로 당연히 count = 0 이다.
                #반면 ret의 길이는 1이므로 B의 기준에서 무언가가 앞에 한개 있어야 하는데 존재하지 않는 것이므로 이 스킬트리는 잘못된 것임을 알 수 있다.
                if count != len(skill[:skill.index(s)]):
                    is_skill = False

                #skill이 CBD이고 임의의 스킬트리 CDA에 대하여, D에서 skill[:skill.index(s)]의 길이는 2인 반면 ret은 C 한개이므로 최대 count = 1이다.
                #따라서 이 경우도 스킬트리는 잘못된 것이다. 반대로, 스킬트리가 CBD이면 B앞에 C, D앞에 BC가 있어 is_skill은 True,
                #BCD이면 B에서 count = 0이고  skill[:skill.index(s)]는 1이므로 is_skill은 False이다.

        if is_skill:
            answer += 1
            
    return answer