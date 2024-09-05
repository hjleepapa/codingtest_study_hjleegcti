def count_word_frequencies(words):
    # 구현하세요
    result = dict()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    
    return result
            
print(count_word_frequencies(["apple", "banana", "apple", "orange", "banana", "apple"]))  
