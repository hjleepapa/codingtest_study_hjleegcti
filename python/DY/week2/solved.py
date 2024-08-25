# 문제 1

def remove_duplicates_and_sort(lst):
    tmp = set(lst)
    return list(tmp)

# 문제 2

def count_word_frequencies(words):
    dic = {}
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

# 문제 3

def key_exists(d, key):
    if key in d:
        return True
    else:
        return False
    
# 문제 4
def sum_of_tuple(tpl):
    return sum(tpl)

# 문제 5
def slice_list(lst, start, end):
    return lst[start:end]

# 예시
print(remove_duplicates_and_sort([4, 2, 2, 1, 3, 4]))  # 출력: [1, 2, 3, 4]
print(remove_duplicates_and_sort([5, 5, 5, 5]))  # 출력: [5]
print(remove_duplicates_and_sort([1, 2, 3, 4, 5]))  # 출력: [1, 2, 3, 4, 5]

# 예시
print(count_word_frequencies(["apple", "banana", "apple", "orange", "banana", "apple"]))  
# 출력: {'apple': 3, 'banana': 2, 'orange': 1}
print(count_word_frequencies(["dog", "cat", "dog", "dog", "fish"]))  
# 출력: {'dog': 3, 'cat': 1, 'fish': 1}


# 예시
print(key_exists({"name": "Alice", "age": 25}, "name"))  # 출력: True
print(key_exists({"name": "Alice", "age": 25}, "address"))  # 출력: False
print(key_exists({}, "key"))  # 출력: False


# 예시
print(sum_of_tuple((1, 2, 3, 4)))  # 출력: 10
print(sum_of_tuple((5,)))  # 출력: 5
print(sum_of_tuple(()))  # 출력: 0


# 예시
print(slice_list([10, 20, 30, 40, 50], 1, 3))  # 출력: [20, 30]
print(slice_list([1, 2, 3, 4, 5], 0, 5))  # 출력: [1, 2, 3, 4, 5]
print(slice_list([7, 8, 9], 1, 1))  # 출력: []