# 주식 가격 (https://school.programmers.co.kr/learn/courses/30/lessons/42584)
# - 다시 풀어볼 문제
def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = i - j
    
    return answer

print(solution([1, 2, 3, 2, 3]))    # [4, 3, 1, 1, 0]