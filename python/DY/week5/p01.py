# 숫자의 각 자리수를 거꾸로 나열하기 
def solution(n, new, cnt, end):
    if cnt == end :
        print(new)
        return n
    tmp = str(n)
    newT = tmp[:len(tmp)-1]
    new += tmp[len(tmp)-1:]
    cnt+=1
    solution(newT, new, cnt, end)
    



tmp = 12345
end = len(str(tmp))
solution(str(tmp), '', 0, end)
