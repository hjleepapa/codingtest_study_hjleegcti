def solution(board, moves):
    #시간 복잡도는 O(N^3)까지 가능함.
    answer = 0
    # 바구니의 크기는 무한대 
    basket = []
    cnt=0
    #print(board)
    for move in moves:
        #print(move)
        for i in board:
            #print(i)
            if i[move-1] != 0: #만약 i 줄 배열에 move칸에 값이 0이 아니라면
                try:
                    a=basket.pop()
                    if a == i[move-1]: 
                        cnt+=2
                        i[move-1] = 0
                    else:
                        basket.append(a)
                        basket.append(i[move-1]) # 바구니에 추가해줌
                        i[move-1] = 0 # 바구니에 추가한 것은 0으로 처리함
                except:
                    basket.append(i[move-1]) # 바구니에 추가해줌
                    i[move-1] = 0 # 바구니에 추가한 것은 0으로 처리함
                
                break # 해당 반복문 탈출 후, 다음 move조회
            else:# 만약 0이면
                continue #  다음 줄로 넘겨서 조회함 
        

    #print('basket', basket)
    #print("cnt", cnt)

    
    return cnt