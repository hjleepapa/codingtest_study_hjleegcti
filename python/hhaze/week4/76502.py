# 괄호 회전하기 (https://school.programmers.co.kr/learn/courses/30/lessons/76502)
def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    answer = 0
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        stack = []
        
        for ch in temp:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(pairs[ch])
            else:
                if not stack:
                    continue
                
                if ch == stack[-1]:
                    stack.pop()
        
        if len(stack) == 0:
            answer += 1
    
    return answer

print(solution("[](){}"))    # 3
print(solution("}]()[}"))    # 2
print(solution("[)(]"))    # 0
print(solution("}}}"))    # 0