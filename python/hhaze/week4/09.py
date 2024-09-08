# 몸풀기 문제: 10진수를 2진수로 변환하기
def solution(num):
    stack = []
    result = ''
    
    while num > 0:
        stack.append(num % 2)
        num //= 2
    
    while len(stack) > 0:
        result += str(stack.pop())
    
    return result

print(solution(10))   # 1010
print(solution(27))   # 11011
print(solution(112345))   # 11000000111001