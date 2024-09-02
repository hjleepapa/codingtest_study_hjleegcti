def solution(tmpList):
    tList=set(tmpList)
    result=list(tList)
    result.sort(reverse=True)
    return result

tmpList=[4, 2, 2, 1, 3, 4]

print(solution(tmpList))
