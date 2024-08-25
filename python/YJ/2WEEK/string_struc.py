#문자열은 immutable object로 수정시 새로운 생성 및 반환
string = "he"
string += "llo"
print(string) # hello

#수정
string = string.replace("l", "t") # l -> t 
print(string)