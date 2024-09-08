def solution(s):
    left1 = [] 
    left2 = [] 
    left3 = [] 
    
    check = [0]*3
    pass1=0
    pass2=0
    
    for i in s:
        if i == '(':
            check[0]+=1
        elif i == '[':
            check[1]+=1
        elif i == '{':
            check[2]+=1
        elif i ==')':
            check[0]-=1
        elif i == ']':
            check[1]-=1
        elif i == '}':
            check[2]-=1
    
    if check[0] ==0 and check[1]==0 and check[2]==0:
        pass1=1
    
    mylist=list(s)
    
    if pass1==0:
        return 0
    
    else:
        thisis = 0
        for i in range(len(s)):
            stakk = [] 

            
            word = mylist.pop()
            mylist.insert(0, word)
            #print(mylist)
            #print("---")
            breakk=0
            for i in mylist:
                #print(i)
                if i == ']':
                    try: 
                        word = stakk.pop()
                        if word == '[':
                            continue
                        else:
                            breakk=1
                            break
                    except:
                        breakk=1
                        break
                elif i == ')':
                    try: 
                        word = stakk.pop()
                        if word == '(':
                            continue
                        else:
                            breakk=1
                            break
                    except:
                        breakk=1
                        break
                elif i == '}':
                    try: 
                        word = stakk.pop()
                        if word == '{':
                            continue
                        else:
                            breakk=1
                            break
                    except:
                        breakk=1
                        break
                elif i == '[':
                    stakk.append('[')
                elif i == '(':
                    stakk.append('(')
                elif i == '{':
                    stakk.append('{')
            
            #print('left[0]', left[0], 'left[1]', left[1], 'left[2]', left[2])
            
            if len(stakk)==0 and len(stakk)==0 and len(stakk)==0 and breakk==0:
                thisis+=1

            
                

        return thisis