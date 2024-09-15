def solution(s, cnt, dic):
    if len(s)==cnt:
        return dic
    
    tmp = s[cnt]
    if s[cnt] not in dic:
        
        dic[tmp]=1
    else:
        dic[tmp]+=1
    cnt+=1
    solution(s, cnt, dic)


s = "aaabccccdd"
dic = {}
solution(s, 0, dic)
printS=''
for key, value in dic.items():
    printS+=key+str(value)

print(printS)