# 짝지어 제거하기 (https://school.programmers.co.kr/learn/courses/30/lessons/12973)
def solution(s):
    answer = 0
    stack = []
    
    for ch in s:
        if not stack:
            stack.append(ch)
        else: 
            if ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
    
    if not stack:
        answer = 1

    return answer

print(solution("baabaa"))    # 1
print(solution("cdcd"))    # 0