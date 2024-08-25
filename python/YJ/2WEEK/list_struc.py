my_list = [1,2,3,4,5]
my_list[4] = 6
print(my_list) # [1, 2, 3, 4, 6]

#리스트 인덱싱
my_list = [1,2,4]

#마지막에 원소 추가
my_list.append(10)
print(my_list) # [1, 2, 4, 10]

#해당 인덱스의 원소 제거
#인덱스 0 원소 제거
del my_list[0]
print(my_list) # [2, 4, 10]

#리스트 슬라이싱, end 인덱스는 미포함
#        -5 -4 -3 -2 -1
my_list = [1,2,3,4,5]
print(my_list[0:2]) # [1, 2]
print(my_list[1:])
print(my_list[-4:-2]) # [2, 3]