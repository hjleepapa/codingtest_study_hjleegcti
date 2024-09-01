# 모의고사 (https://school.programmers.co.kr/learn/courses/30/lessons/42840)
def solution(answers):
    result = [0, 0, 0]
    
    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, answer in enumerate(answers):
        if num_1[i % len(num_1)] == answer:
            result[0] += 1
        if num_2[i % len(num_2)] == answer:
            result[1] += 1
        if num_3[i % len(num_3)] == answer:
            result[2] += 1
    
    return [i + 1 for i, value in enumerate(result) if value == max(result)]

print(solution([1, 2, 3, 4, 5]))    # [1]
print(solution([1, 3, 2, 4, 2]))    # [1, 2, 3]