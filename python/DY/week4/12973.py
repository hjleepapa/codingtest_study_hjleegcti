def solution(s):
    #O(nLogN)으로 구현
    answer = -1

    #print(s)
    stakk =[]
    
    newS=s
    newS=list(newS)
    
    for i in range(len(newS)):
        
        
        if i == 0 or len(stakk)==0:
            stakk.append(newS[i])
        else:
            a = stakk.pop()
            if newS[i] == a:
                continue
            else:
                stakk.append(a)
                stakk.append(newS[i])
    
    if len(stakk)==0:
        return 1
    else:
         return 0   

    
    return answer