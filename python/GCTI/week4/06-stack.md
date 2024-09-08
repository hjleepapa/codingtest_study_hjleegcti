06-1 스택 개념

FIFO(First In Last Out). 스택에 삽입하는 연산을 push, 꺼내는 것을 pop.

06-2 스택 정의

push, pop, isFull, isEmpty와 같은 연산을 정의. 최근 삽입한 데이타 위치를 저장변수:top

06-3 몸풀기 문제

문제08 괄호 짝 맞추기
(())() => True
((())() => False

통상 parentheses question은 stack을 이용한다. 여기에 hashmap을 이용해서 d = {')':'('}, close:open을 이용하면 혹시 괄호의 모양이 여러가지가 나오는 경우라 하더라도 용이한 해결을 할수 있다. for loop 를 이용해서 입력 string의 character를 하나씩 이동하며 open 기호를 스택에 넣고 맞는 close 기호가 나오면 스택에 들어있던 open을 pop시키면서 dict에 들어있던 key:value로 같은지를 비교해 상쇄하는 logic을 사용하면 된다.

def solution(s):
    stack = []
    d = {')':'('}
    
    for c in s:
        if c not in d: # open bracket
            stack.append(c)
        else: # close bracket
            if not stack: # too many close bracket
                return False
            else:
                open_bracket = stack.pop()
                if open_bracket != d[c]:
                    return False
    return len(stack) == 0

print(solution("((())()"))


문제 09 10진수를 2진수로 변환하기

10진수를 2진수로 변환하기

def solution(n):
    stack = []
    while n > 0:
        t = n % 2
        n = n // 2
        stack.append(str(t))
    print(stack[::-1])
    
    binary = "".join(stack[::-1])
    return int(binary)

print(solution(4))

06-4 합격자가 되는 모의 테스트

문제 10 괄호 회전하기

TC: O(n^2)
def solution(s):
    res = 0
    n = len(s)
    d = {')':'(', ']':'[', '}':'{'} # define matching pairs
    
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i + j) % n]
            if c not in d: # open bracket
                stack.append(c)
            else: # close bracket
                if not stack: # too many close bracket
                    break
                else: # check matching brackets
                    open_bracket = stack.pop()
                    if open_bracket != d[c]: # not match
                        break
        else:
            if len(stack) == 0:
                res += 1
    return  res

print(solution("}]()[{"))

문제 11 짝지어 제거하기
"baabaa" => 1
"cdcd" => 0
TC: O(n)

def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    return  int(len(stack) == 0)

print(solution("cdcd"))

문제 12 주식가격

[1,2,3,2,3] => [4,3,1,1,0]

주식가격이 있는 prices = [1,2,3,2,3] 가 주어지고 그 시점에서 가격이 떨어지지 않는 기간은 각각 얼마인지 return

주식가격이 최초 떨어지는 지점을 이용해 다른 포인트에서의 길이, 즉 가격이 떨어지지 않는 기간을 계산. 예를 들면 다음포인트에서 바로 가격이 떨어지면 1, 다음다음포인트에서 가격이 떨어지면 2, 다음 가격이 없으면 0.

이문제는 값이 계속해서 올라가는 동안에는 스택에 계속 push를 하고 떨어지는 지점에서 멈춰 while loop를 돌며 스택의 마지막 값을 그 전의 값들을 계속해서 비교해서 그 스택을 pop시키며 그 전의 큰값들을 제거해 나가는 방식으로 이를 Monotonic descresing stack이라고 부른다.

def solution(prices):
    stack = []
    n = len(prices)
    res = [0] * n
    
    stack = [0] #initialize stack to compare previous val with cur val
    
    for i in range(1,n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        res[j] = n - (j+1)
    return res

print(solution([1,6,9,5,3,2,7]))

문제 13 크레인 인형 뽑기 게임

board
moves
result
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
[1,5,3,5,1,2,1,4]
4
convert board array to stack

<Pseudo-code>
if not bucket:
    bucket.append(doll)
else:
    if bucket and bucket[-1] == stack_n.pop():
        bucket.pop()
        count += 1
    else:
        bucket.append(doll)
return len(bucket)

def solution(board, moves):
    m = len(board)
    n = len(board[0])
    
    lanes = [[] for _ in range(n)] # convert 2D array board to lanes
    
    for i in range(m - 1, -1, -1):
        for j in range(n):
            if board[i][j]:
                lanes[j].append(board[i][j])
    
    bucket = []
    
    res = 0
    
    for k in moves:
        if lanes[k - 1]: # if doll exists:
            doll = lanes[k - 1].pop()
            
            if bucket and bucket[-1] == doll:
                bucket.pop()
                res += 2
            else: # no doll in bucket or different doll
                bucket.append(doll)
                
    return res
    

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], 
[1,5,3,5,1,2,1,4]))


================================================================================================================


질문
1. 스택을 이용하여 주어진 문자열을 뒤집는 알고리즘을 설계하고 구현해 보세요. 이 알고리즘의 시간 복잡도와 공간 복잡도는 각각 어떻게 되나요?
TC: O(n) => 2n for loop + while loop = > n
SC: O(n) => stack, res are 2n => n
def solution(str1):
    stack = []
    res = []
    for ch in str1:
        stack.append(ch)
    
    while stack:
        res.append(stack.pop())
    
    return "".join(res)
solution("abcde")

스택을 사용하지 않고도 문자열을 뒤집을 수 있는 다른 방법을 설명해 보세요.
use simple string slicing: [::-1]

def solution(str1):
    return str1[::-1]
solution("abcde")

2. 스택이 재귀적인 함수 호출과 어떻게 관련이 있는지 설명해 보세요.
def factorial(n):
    if n == 1:                
        return 1              
    else:
        return n * factorial(n - 1)

print(factorial(3))

위와 같은 팩토리얼을 계산하는 recursion function을 보면 factorial 함수를 계속해서 호출될때 마다 함수를 위한 메모리가 계속해서 할당된다. 함수가 호출될 때마다 쓰는 temporary memory를 stack.
stack은 LIFO(후입선출) 구조이기 때문에 가장 마지막에 호출된 함수 factorial(1)를 먼저 완료하고, 값을 아래로 전달하여 최초로 호출된 함수 factorial(3)가 최종 값을 계산한다.


2. 재귀 함수를 스택을 사용하여 비재귀적으로 변환하는 방법을 예시를 통해 설명할 수 있나요?
stack을 이용하면 아래처럼 첫번째 while loop는 스택에 n부터 1까지 차례로 집어넣고 두번째 while loop는 스택에 있는 것을 맨 위에서부터 꺼내면서 1부터 n까지의 곱을 계산하는 연산을 수행하면 재귀함수를 쓰는 것과 동일한 결과를 얻을 수 있다.
def factorial(n):
    stack = []
    
    while n > 0:
        stack.append(n)
        n -= 1
    
    total = 1
    while len(stack) > 0:
        total *= stack.pop()
    
    return total
    
print(factorial(5))


실전 문제

문제 1: HTML 태그 유효성 검사
HTML 문서에서 태그가 올바르게 열리고 닫혔는지 확인하는 프로그램을 작성하세요. <tag> 형태로 열리고 </tag> 형태로 닫혀야 합니다. 태그 이름은 영문 소문자만 사용됩니다.
입력: HTML 태그가 포함된 문자열이 주어집니다.
출력: 태그가 올바르게 열리고 닫혔다면 True, 그렇지 않다면 False를 출력합니다.
예시 입력/출력
# 예시 입력 1 "<div><p>Hello</p></div>" 
# 예시 출력 1 True
# 예시 입력 2 "<div><span>Hi</div></span>" 
# 예시 출력 2 False
입출력 설명
예시 1에서는 <div> 태그가 <p> 태그를 포함하고, 올바르게 닫히므로 True를 반환합니다.
예시 2에서는 <span> 태그가 <div> 태그 내에서 닫히기 때문에 구조가 올바르지 않아 False를 반환합니다.

def solution(s):
    stack = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '<' and s[i+1] != '/': # opening tag
            j = i + 1
            while j < n and s[j] != '>':
                j += 1
            if j < n:
                tag = s[i:j+1]
                if tag[-2] != '/': # check self-closing
                    stack.append(tag)
                i = j
        
        elif s[i] == '<' and s[i+1] == '/': # closing end
            j = i + 2
            while j < n and s[j] != '>':
                j += 1
            if j < n:
                end = s[i:j+1]
                if not stack or stack[-1][1:] != end[2:]:
                    return False
                stack.pop()
                i = j
        i += 1
        
    return len(stack) == 0

print(solution("<div><span>Hi</div></span>"))

문제 2: 역순 이진수 표현
주어진 양의 정수를 이진수로 변환한 후, 그 이진수를 뒤집어 정수로 다시 변환한 결과를 출력하는 프로그램을 작성하세요.
입력: 하나의 양의 정수 N이 주어집니다.
출력: 이진수를 뒤집어 변환한 결과 정수를 출력합니다.
예시 입력/출력
# 예시 입력 1
13
# 예시 출력 1
11
# 예시 입력 2
4
# 예시 출력 2
1
입출력 설명
예시 1에서 13의 이진수 표현은 1101이고, 이를 뒤집으면 1011이 되어 10진수로 11입니다.
예시 2에서 4의 이진수 표현은 100이고, 이를 뒤집으면 001이 되어 10진수로 1입니다.

스택에 입력숫자를 2로 나눈 나머지를 계속해서 넣으면 스택에 들어있는 숫자 그 순서가 역으로 뒤집은 것이 되므로 그것을 그대로 join해서 가져와서 binary를 decimal로 바꾸는 과정을 거치면 된다.

def reverse_bi_digit(n):
    stack = []
    
    while n > 0:
        t = n % 2
        n = n // 2
        stack.append(str(t))
    print(stack)
    reverse_binary = int("".join(stack))
    
    decimal = 0
    p = 1
    while reverse_binary > 0:
        t = reverse_binary % 10
        reverse_binary = reverse_binary // 10
        decimal += t * p
        p = p * 2
        
    return decimal
print(reverse_bi_digit(13))
