def solution(answers):
    answer = []
    
    l1=[1,2,3,4,5]
    l2=[2,1,2,3,2,4,2,5]
    l3=[3,3,1,1,2,2,4,4,5,5]
    
    len_a = len(answers)
    cnt = 0
    score1 = score2 = score3 = 0
    for i in range(len(answers)):
        cnt = i
        if cnt >= len(l1):
            cnt = cnt % len(l1)
        if l1[cnt] == answers[i]:
            score1+=1 
            
    cnt = 0  
    for i in range(len(answers)):
        cnt = i
        if cnt >= len(l2):
            cnt = cnt % len(l2)
        if l2[cnt] == answers[i]:
            score2+=1 

    cnt = 0
    for i in range(len(answers)):
        cnt = i
        if cnt >= len(l3):
            cnt = cnt % len(l3)
        if l3[cnt] == answers[i]:
            score3+=1 

    total_list=[]
    total_list.append(score1)
    total_list.append(score2)
    total_list.append(score3)
    
    if score1==score2==score3:
        answer.extend([1,2,3])
    else:
        maxx=(max(total_list))
        answer.append(total_list.index(max(total_list)) + 1)
        total_list[total_list.index(max(total_list))] = 0
        if maxx in total_list:
            answer.append(total_list.index(maxx)+1)

    return answer