def trans(target, cnt, result):
    if cnt == len(target):
        print(result)
        return result
    if target[len(target)-cnt-1]== str(1):
        result+=(2**cnt)
    
    cnt+=1
    trans(binary_str, cnt, result)

binary_str = "1101"
trans(binary_str, 0, 0)

