import math

# 문제 1: 숫자의 각 자리수를 거꾸로 나열하기
def solution(n):
    if n < 10:
        return n
    
    last = n % 10
    num = n // 10
    l = len(str(num))
    
    return last * (10 ** l) + solution(num)

print(solution(12345))

# 문제 2: 이진수를 십진수로 변환하기
def solution(binary_str):
    if len(binary_str) == 1:
        return int(binary_str)
    
    first = int(binary_str[0])
    power = len(binary_str) - 1
    binary_str = binary_str[1:]

    return first * (2 ** power) + solution(binary_str)

print(solution("1101"))

# 문제 3: 문자열 압축하기
def solution(s):
    if not s:
        return ""
    
    first = s[0]
    count = 1
    i = 1
    
    while i < len(s) and s[i] == first:
        count += 1
        i += 1
    
    s = s[i:]
    
    return first + str(count) + solution(s)

print(solution("aaabccccdd"))

# 문제 4: 하노이의 탑 문제
def solution(N, from_, to_, via_):
    if N == 1:
        print(f"Move disk {N} from {from_} to {to_}")
    else:
        solution(N - 1, from_, via_, to_)
        print(f"Move disk {N} from {from_} to {to_}")
        solution(N - 1, via_, to_, from_)

print(solution(3, 'A', 'C', 'B'))

# 문제 5: 숫자 분해하기
def solution(n, i=1, result=None):
    if result is None:
        result = []

    if i > math.sqrt(n):
        return result

    if n % i == 0:
        j = n // i
        result.append((i, j))
        
    return solution(n, i + 1, result)

print(solution(12))