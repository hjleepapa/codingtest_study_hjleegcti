# 스택을 이용하여 주어진 문자열을 뒤집는 알고리즘
def solution(str):
    stack = []
    result = ''

    for c in str:
        stack.append(c)
    
    while len(stack) > 0:
        result += stack.pop()
    
    return result

print(solution('abc'))

# 스택을 사용하지 않고도 문자열을 뒤집을 수 있는 방법
def solution(str):
    return ''.join(reversed(str))

print(solution('abc'))

# 문제 1: HTML 태그 유효성 검사
def solution(str):
    stack = []
    i = 0

    while i < len(str):
        if str[i] == '<':
            j = str.find('>', i + 1)

            if j == -1:
                return False
            
            tag = str[i + 1:j]

            if tag.startswith('/'):
                if not stack or (stack.pop() != tag[1:]):
                    return False
            else:
                stack.append(tag)
            
            i = j
        i += 1
    
    return len(stack) == 0

print(solution("<div><p>Hello</p></div>"))
print(solution("<div><span>Hi</div></span>"))

# 문제 2: 역순 이진수 표현
def num_to_stack(num):
    stack = []
    
    if num == 0:
        stack.append(0)
    
    while num > 0:
        stack.append(num % 2)
        num //= 2
    
    return stack

def stack_to_dec(stack):
    result = 0
    i = 0

    while len(stack) > 0:
        n = stack.pop()
        result += (n * (2 ** i))
        i += 1
    
    return result

def solution(num):
    stack = num_to_stack(num)
    dec = stack_to_dec(stack)

    return dec

print(solution(13))
print(solution(4))