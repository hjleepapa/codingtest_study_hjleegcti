def solution(N, stages):
    answer = []
    # 도전 
    # 스테이지 별 도전자 수를 구함 
    challenger = [0] * (N+2)
    for stage in stages:
        challenger[stage] += 1
    
    fails = { }
    total = len(stages)
    
    for i in range(1, N+1):
        if challenger[i]==0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total=total-challenger[i]
            
    #print(fails)
    
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    #값을 기준으로 키를 정렬해서 반환함 
    
    #print(result)
    
    return result