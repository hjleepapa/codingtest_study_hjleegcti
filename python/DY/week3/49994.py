def solution(dirs):
    answer = 0
    
    c = [[0]*11 for _ in range(11)]
    arr=[]
    now = [5, 5]
    
    result = set()
    
    for dir in dirs:
        n1, n2 = now[0], now[1]
        if dir == "U":
            now[1]+=1
            if now[1]==11:
                now[1]=10
                
        elif dir == "D":
            now[1]-=1
            if now[1]==-1:
                now[1]=0
                
        elif dir == "L":
            now[0]-=1
            if now[0]==-1:
                now[0]=0
                
        elif dir == "R":
            now[0]+=1
            if now[0]==11:
                now[0]=10
        xtox, ytoy = now[0], now[1]
        if n1==xtox and n2==ytoy:
            pass
        else:
            result.add((n1, n2, xtox, ytoy))
            result.add((xtox, ytoy, n1, n2))
    answer=len(result)/2
    
    return answer