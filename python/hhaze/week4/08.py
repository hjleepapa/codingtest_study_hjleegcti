# 몸풀기 문제: 괄호 짝 맞추기
def solution(str):
    stack = []

    for c in str:
        if c == '(':
            stack.append(')')
        else:
            if not stack or (stack.pop() != c):
                return False
    
    return len(stack) == 0

print(solution("(())()"))    # True
print(solution("(()))()"))    # False