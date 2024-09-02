def solution(arr1, arr2):
    answer = [[]]
    
    n1 = len(arr1)
    m1 = len(arr1[0])
    
    n2 = len(arr2)
    m2 = len(arr2[0])
    
    tmp=[]
    for i in range(n1):
        tmpL=[]
        for jj in range(m2):
            sum = 0
            for j in range(m1):
                sum+=arr1[i][j]* arr2[j][jj]
            tmpL.append(sum)
        tmp.append(tmpL)
        
    
    return tmp