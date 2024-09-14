Recursion

자기 자신을 호출하여 더 작은 하위 문제를 해결하는 함수로서 이를 이용해서 문제를 반복적으로 분해하다가 더 이상 내려갈수 없는 base condition을 만나면 해당값을 리턴하면서 다시 윗쪽으로 올라가며 아래에서 구해진 값을 계속적으로 리턴하면서 최종 결과값을 얻는 방법.

장점: 반복패턴을 이용해 코드가 간결
단점: 너무 깊은 재귀호출로 스택오버플로우 발생

1. 재귀 깊이를 줄이기 위한 방법:
memoization: 이전값을 저장해 두었다가 재사용 하는 기법

memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

2. 재귀함수 구현 절차
 1. base condition
 2. 더 작은 문제로 분할
 3. 재귀 호출

def factorial(n):
    # 1. base condition
    if n == 0 or n == 1:
        return 1
    # 2. move to deeper level
    else:
        return n * factorial(n - 1)

3. 재귀함수 구현시 주의
 1. set base condition to avoid stack overflow
 2. consider depth of stack
 3. use memoization which keeps previously calcuated values

=============================================================================

3. 실전 문제

문제 1: 숫자의 각 자리수를 거꾸로 나열하기
문제 설명:
양의 정수 n이 주어졌을 때, n의 각 자리수를 재귀를 사용하여 거꾸로 나열한 값을 반환하는 함수를 작성하세요.
예시 입/출력:
입력: n = 12345
출력: 54321
설명:
정수 12345를 재귀적으로 처리하여 54321이 반환됩니다.
제한 사항:
n은 1 이상 1,000,000 이하의 자연수입니다.

def reverse_num(n, rem):
    if n == 0:
        return rem
    else:
        return reverse_num(n // 10, rem * 10 + n % 10)

print(reverse_num(12345, 0))

문제 2: 이진수를 십진수로 변환하기
문제 설명:
이진수로 표현된 문자열이 주어졌을 때, 해당 이진수를 재귀를 사용하여 십진수로 변환하는 함수를 작성하세요.
예시 입/출력:
입력: binary_str = "1101"
출력: 13
설명:
이진수 1101은 십진수로 변환하면 13이 됩니다.
제한 사항:
문자열의 길이는 1 이상 32 이하입니다.
이진수는 0과 1로만 구성되어 있습니다.

def bi_to_decimal(n, p=1):
    n = int(n)
    if n == 0:
        return 0
    else:
        rem = n % 10
        rem = rem * p
        return rem + bi_to_decimal(n // 10, p * 2)   

print(bi_to_decimal("1101"))

문제 3: 문자열 압축하기
문제 설명:
문자열이 주어졌을 때, 재귀를 사용하여 동일한 문자가 연속될 경우 그 문자의 반복 횟수를 세어 압축한 문자열을 반환하는 함수를 작성하세요.
예시 입/출력:
입력: s = "aaabccccdd"
출력: "a3b1c4d2"
설명:
연속된 문자를 카운트하여 "a3b1c4d2"가 반환됩니다.
제한 사항:
문자열의 길이는 1 이상 1,000 이하입니다.

def supress_str(s, i=0, cnt=1):
    n = len(s)
    
    if not s:  
        return ""
    
    elif i == n - 1:
        return s[i] + str(cnt)
        
    elif len(s) == 1:
        return s 
        
    elif s[i] == s[i+1]:
        cnt += 1
        return supress_str(s, i+1, cnt)
    
    else: 
        
        return  s[i] + str(cnt) + supress_str(s, i+1, 1)
 
print(supress_str("aaabccccdd"))

문제 4: 하노이의 탑 문제
문제 설명:
3개의 기둥과 N개의 원판이 주어졌을 때, 재귀를 사용하여 하노이의 탑 문제를 해결하는 알고리즘을 작성하세요. 모든 원판을 첫 번째 기둥에서 세 번째 기둥으로 옮기는 과정을 출력하세요.
예시 입/출력:
입력: N = 3
출력:
Move disk 1 from A to C Move disk 2 from A to B Move disk 1 from C to B Move disk 3 from A to C Move disk 1 from B to A Move disk 2 from B to C Move disk 1 from A to C
제한 사항:
원판의 개수 N은 1 이상 20 이하입니다.

def tower_hanoi(N, a, b, c):
    
    if N == 1:
        print("Move disk 1 from ", a, "to", c)
        return
    
    tower_hanoi(N - 1, a, c, b)
    print("Move disk", N, "from ", a, "to", c)
    tower_hanoi(N - 1, b, a, c)
 
print(tower_hanoi(3, "A", "B", "C"))

문제 5: 숫자 분해하기
문제 설명:
양의 정수 n이 주어졌을 때, n을 두 정수의 곱으로 분해하는 모든 방법을 찾는 재귀 함수를 작성하세요.
예시 입/출력:
입력: n = 12
출력: [(1, 12), (2, 6), (3, 4)]
설명:
12를 두 정수의 곱으로 나타내면 (1, 12), (2, 6), (3, 4)와 같이 분해됩니다.
제한 사항:
n은 1 이상 10,000 이하의 정수입니다.

def divide_two_nums(n, i = 1, res=None):
    res = []
    
    if n <= 2:
        res.append((1, n))
        
    elif n % i == 0 and i * i < n:
        res.append((i, n // i))
        res.extend(divide_two_nums(n, i+1))
        
    return res
 
print(divide_two_nums(24))
