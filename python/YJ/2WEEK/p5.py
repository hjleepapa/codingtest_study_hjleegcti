# 리스트 lst와 두 개의 정수 start, end가 주어졌을 때, 주어진 범위에 해당하는 부분 리스트를 반환하는 함수를 작성하세요. start 인덱스는 포함되며, end 인덱스는 포함되지 않습니다.

def slice_list(lst, start, end):
    return lst[start:end]


print(slice_list([7, 8, 9], 1, 1))  # 출력: []
print(slice_list([10, 20, 30, 40, 50], 1, 3))  # 출력: [20, 30]
