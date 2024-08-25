# 문제 1
def remove_duplicates_and_sort(list):
    return sorted(set(list))

print(remove_duplicates_and_sort([4, 2, 2, 1, 3, 4]))
print(remove_duplicates_and_sort([5, 5, 5, 5]))
print(remove_duplicates_and_sort([1, 2, 3, 4, 5]))

# 문제 2
def count_word_frequencies(words):
    my_dict = {}
    
    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    
    return my_dict

print(count_word_frequencies(["apple", "banana", "apple", "orange", "banana", "apple"]))
print(count_word_frequencies(["dog", "cat", "dog", "dog", "fish"]))  

# 문제 3
def key_exists(d, key):
    return key in d

print(key_exists({"name": "Alice", "age": 25}, "name"))
print(key_exists({"name": "Alice", "age": 25}, "address"))
print(key_exists({}, "key"))

# 문제 4
def sum_of_tuple(tpl):
    sum = 0

    for t in tpl:
        sum += t
    
    return sum

print(sum_of_tuple((1, 2, 3, 4)))
print(sum_of_tuple((5,)))
print(sum_of_tuple(()))

# 문제 5
def slice_list(lst, start, end):
    return lst[start:end]

print(slice_list([10, 20, 30, 40, 50], 1, 3))
print(slice_list([1, 2, 3, 4, 5], 0, 5)) 
print(slice_list([7, 8, 9], 1, 1))