def solution(prices):
    answer = []
    total = len(prices)
    answer = [0] * total
    #각 초 시점의 길이를 넣을 배열
    stackk = [0] 

    # 스택을 0으로 초기화 한 이유는 순회를 인덱스 1부터 하기 위해서임 
    # prices의 0번 인덱스는 스택에 넣고 시작한다. 
    
    for i in range(1, total):
        # 1부터 total까지 순회한다. 
        # 0번 인덱스부터 total 인덱스까지 순회할 때, 가격의 증가만 있다면,
        # 계속 stackk에 넣는다. 
        # 만약 가격이 떨어진다면 그때부터는 스택에서 꺼내어서 하락한 가격의 인덱스로부터 길이를 구한다. 
        while stackk and prices[stackk[-1]]>prices[i]:
            a=stackk.pop()
            answer[a]=i-a
        stackk.append(i)
        
    while stackk: # 스택이 빌 때까지 순회하여 길이를 찾아준다. 
    #이 스택은 최종적으로 증가한 값들만 남아있다. 
        a=stackk.pop()
        answer[a]=total-a-1
        
    #print(answer)
    
    return answer