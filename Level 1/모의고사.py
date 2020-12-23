def solution(answers):
    #학생 1,2,3의 한바퀴만 리스트로 생성
    student_1 = [1,2,3,4,5,1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    #학생1,3은 한바퀴에 10개, 학생2는 한바퀴에 8개이므로 인덱스를 두개 생성
    idx1 = 0
    idx2 = 0 
    
    #딕셔너리로 만들고, 해당될때마다 학생의 점수를 += 1
    student_ans = {}
    student_ans[1] = 1
    student_ans[2] = 1
    student_ans[3] = 1
    
    for ans in answers:
        if student_1[idx1] == ans:
            student_ans[1] += 1
        if student_3[idx1] == ans:
            student_ans[3] += 1
        if student_2[idx2] == ans:
            student_ans[2] += 1
    
        idx1 += 1
        idx1 = idx1 % 10
        idx2 += 1
        idx2 = idx2 % 8
    
    #(학생, 학생의 점수)를 원소로 하는 리스트 생성
    result = list(student_ans.items())

    # 맞춘 개수의 최댓값
    maximum = max(student_ans.values())
    
    answer = []
    for i in range(3):
        # 학생의 맞춘 개수가 최댓값과 같다면 answer에 추가
        if result[i][1] == maximum:
            answer.append(result[i][0])
            
    return answer