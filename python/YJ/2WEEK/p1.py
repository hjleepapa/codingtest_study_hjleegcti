# 리스트 lst가 주어졌을 때, 리스트 내 중복된 요소를 제거하고 남은 요소들을 오름차순으로 정렬한 새로운 리스트를 반환하는 함수를 작성하세요.
def remove_duplicates_and_sort(lst):
    return sorted(set(lst))

print(remove_duplicates_and_sort([4, 2, 2, 1, 3, 4]))