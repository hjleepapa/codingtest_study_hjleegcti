def checkValid(str):
    tmpSTR=''
    for i in str:

        if i =='<':
            check = 1
    
        if i == '>':
            check = 0
            tmpS.append(tmpSTR)
            tmpSTR=''
        if i =='<' or i=='/':
            pass
        else:
            if check == 1:
                tmpSTR+=i


tmpS = []
str = '<div><p>Hello</p></div>'
checkValid(str)

rem = 0
check2=0
end = 0
while 1:
    if len(tmpS)<2:
        break

    for i in range(len(tmpS)-1):
        if tmpS[i] == tmpS[i+1]:
            rem = i
            check2 = 1
            break

    if check2 ==1:
        del tmpS[i]
        del tmpS[i]
        check2 = 0
    else:
        end = 1
        break

if len(tmpS)==0:
    print(True)
else:
    print(False)
