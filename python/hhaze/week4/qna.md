# 질문

1. 스택을 이용하여 주어진 문자열을 뒤집는 알고리즘을 설계하고 구현해 보세요. 이 알고리즘의 시간 복잡도와 공간 복잡도는 각각 어떻게 되나요? 스택을 사용하지 않고도 문자열을 뒤집을 수 있는 다른 방법을 설명해 보세요.

    - 스택을 이용하여 주어진 문자열을 뒤집는 알고리즘
        ```python
        def solution(str):
            stack = []
            result = ''

            for c in str:
                stack.append(c)
            
            while len(stack) > 0:
                result += stack.pop()
            
            return result
        ```
        - 시간 복잡도: O(N)
            - for 문 O(N) 그리고 while 문 O(N)
        - 공간 복잡도: O(N)
            - 스택 O(N) 그리고 문자열 O(N)

    - 스택을 사용하지 않고도 문자열을 뒤집을 수 있는 방법
        ```python
        def solution(str):
            return ''.join(reversed(str))
        ```
        - 내장 함수 사용

2. 스택이 재귀적인 함수 호출과 어떻게 관련이 있는지 설명해 보세요. 재귀 함수를 스택을 사용하여 비재귀적으로 변환하는 방법을 예시를 통해 설명할 수 있나요?

    - 스택이 재귀적인 함수 호출과 어떻게 관련이 있는지
        - 재귀 함수가 호출될 때 스택이 생성되어 콜 스택에 쌓이는 구조
        - 호출된 함수가 일을 마친 후에 돌아갈 주소도 스택에 저장
    - 재귀 함수를 스택을 사용하여 비재귀적으로 변환하는 방법
        ```python
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        ```

        ```python
        def factorial_with_stack(n):
            stack = []
            result = 1
            
            while n > 1 or stack:
                if n > 1:
                    stack.append(n)
                    n -= 1
                else:
                    result *= stack.pop()
            
            return result
        ```


# 실전 문제
## 문제 1: HTML 태그 유효성 검사
HTML 문서에서 태그가 올바르게 열리고 닫혔는지 확인하는 프로그램을 작성하세요. `<tag>` 형태로 열리고 `</tag>` 형태로 닫혀야 합니다. 태그 이름은 영문 소문자만 사용됩니다.
- 입력: HTML 태그가 포함된 문자열이 주어집니다.
- 출력: 태그가 올바르게 열리고 닫혔다면 `True`, 그렇지 않다면 `False`를 출력합니다.

### 예시 입력/출력
```
# 예시 입력 1
"<div><p>Hello</p></div>"

# 예시 출력 1
True

# 예시 입력 2
"<div><span>Hi</div></span>"

# 예시 출력 2
False
```

### 입출력 설명
- 예시 1에서는 `<div>` 태그가 `<p>` 태그를 포함하고, 올바르게 닫히므로 `True`를 반환합니다.
- 예시 2에서는 `<span>` 태그가 `<div>` 태그 내에서 닫히기 때문에 구조가 올바르지 않아 `False`를 반환합니다.

```python
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
```

## 문제 2: 역순 이진수 표현
주어진 양의 정수를 이진수로 변환한 후, 그 이진수를 뒤집어 정수로 다시 변환한 결과를 출력하는 프로그램을 작성하세요.
- 입력: 하나의 양의 정수 N이 주어집니다.
- 출력: 이진수를 뒤집어 변환한 결과 정수를 출력합니다.

### 예시 입력/출력
```
# 예시 입력 1
13

# 예시 출력 1
11

# 예시 입력 2
4

# 예시 출력 2
1
```

### 입출력 설명
- 예시 1에서 13의 이진수 표현은 1101이고, 이를 뒤집으면 1011이 되어 10진수로 11입니다.
- 예시 2에서 4의 이진수 표현은 100이고, 이를 뒤집으면 001이 되어 10진수로 1입니다.

```python
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
```