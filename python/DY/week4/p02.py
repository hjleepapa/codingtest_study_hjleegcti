
def trans(n):
    binary = bin(n)
    binary = binary[2:]
    rbinary = binary[::-1]
    
    ret = int(rbinary, 2)
    return ret

tmp=13
print(trans(tmp))