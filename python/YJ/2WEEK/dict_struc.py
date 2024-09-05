#key, value 쌍으로 데이터를 저장, 해시 테이블로 구현

my_dict = {}
my_dict["apple"] = 1
my_dict["banana"] = 3
print(my_dict) # {'apple': 1, 'banana': 3}

key = "apple"
if key in my_dict:
    value = my_dict[key]
    print(f"{key} : {value}") # apple : 1
else:
    print(f"{key} not in dict")


#딕셔너리 수정
my_dict["banana"] = 10
print(my_dict) # {'apple': 1, 'banana': 10}

#딕셔너리 삭제
del my_dict["apple"]
print(my_dict) # {'banana': 10}

#존재하지 않는 키 값을 삭제하려고 하면 예외가 발생하므로 예외 처리 필요
# del my_dict["kiwi"] # KeyError: 'kiwi'

key = "kiwi"
if key in my_dict:
    del my_dict[key]
else:
    print(f"해당 키 {key}는 존재하지 않습니다.") # 해당 키 kiwi는 존재하지 않습니다.
