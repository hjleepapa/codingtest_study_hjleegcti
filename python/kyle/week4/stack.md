
# 목차

1. [질문](#질문)
2. [실전 문제](#실전-문제)

---

##  질문

1. 스택을 이용하여 주어진 문자열을 뒤집는 알고리즘을 설계하고 구현해 보세요. 이 알고리즘의 시간 복잡도와 공간 복잡도는 각각 어떻게 되나요? 스택을 사용하지 않고도 문자열을 뒤집을 수 있는 다른 방법을 설명해 보세요.

# 답
```python
def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string
```

시간복잡도 : 문자열의 갯수가 n일 때, 따라 최악의 경우 반복문이 2n번 동작해야 하므로 시간복잡도는 O(n)

스택을 사용하지 않는다면 문자열을 역순으로 출력하여 해결할 수 있음

```python
def reverse_string(string):
    print(string[::-1])
```



2. 스택이 재귀적인 함수 호출과 어떻게 관련이 있는지 설명해 보세요. 재귀 함수를 스택을 사용하여 비재귀적으로 변환하는 방법을 예시를 통해 설명할 수 있나요?

- 재귀 함수는 호출할 때 마다 함수를 위한 메모리가 추가로 할당된다. 그리 함수가 호출될 떄 할당되는 메모리 영역이 스택이다.
- 팩토리얼 함수를 예로 들면, 스택은 LIFO 구조이기 때문에 가장 마지막에 호출된 factorial(1)부터 -> factorial(n)까지 값을 전달하며 올라간다.
- 재귀 함수를 사용하면 호출 횟수에 제한이 있는데, 이 호출 횟수는 스택의 공간 제한과 관련이 있다. 스택 영역의 공간을 넘어서면 스택 오버플로우거 발생한다.

- 리눅스의 스택 프레임은 아래와 같은 구조를 가진다.
	- ESP(스택의 최상단을 가리키는 포인터)
	- return address
	- 함수의 매개변수
	- 함수의 로컬변수

## 재귀함수
```python
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
```

## 스택을 이용한 비재귀
```python
def factorial(n):
    stack = []
    for i in range(n,1,-1):
        stack.append(i)
    
    result = 1
    for j in range(len(stack)):
        result *= stack.pop()
    
    return result
```


---

## 실전 문제

### 문제 1: HTML 태그 유효성 검사

HTML 문서에서 태그가 올바르게 열리고 닫혔는지 확인하는 프로그램을 작성하세요. `<tag>` 형태로 열리고 `</tag>` 형태로 닫혀야 합니다. 태그 이름은 영문 소문자만 사용됩니다.

- **입력**: HTML 태그가 포함된 문자열이 주어집니다.
- **출력**: 태그가 올바르게 열리고 닫혔다면 `True`, 그렇지 않다면 `False`를 출력합니다.

#### 예시 입력/출력

```python
# 예시 입력 1
"<div><p>Hello</p></div>"

# 예시 출력 1
True

# 예시 입력 2
"<div><span>Hi</div></span>"

# 예시 출력 2
False
```

#### 입출력 설명

- 예시 1에서는 `<div>` 태그가 `<p>` 태그를 포함하고, 올바르게 닫히므로 `True`를 반환합니다.
- 예시 2에서는 `<span>` 태그가 `<div>` 태그 내에서 닫히기 때문에 구조가 올바르지 않아 `False`를 반환합니다.


## 답
GPT도 활용해보고 다른 풀이를 검색을 좀 해보았는데도 잘 이해가 안돼요.
좀더 공부해서 보충해보겠습니다.
```python
def parsing_html(html):
    stack = []
    i = 0
    
    for i in range(len(html)):
        if html[i] == '<':
            j = i+1
            if j < len(html) and html[j] == '/':
                closing = True
                j += 1
            else:
                closing = False
                
            tag_name_start_position = j
            while j < len(html) and html[j] != '>':
                j += 1
            if j == len(html):
                return False
            tag = html[tag_name_start_position:j]
            
            if closing:
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
            else:
                stack.append(tag)            
                
    if stack == []:
        return True
    return False
```

### 문제 2: 역순 이진수 표현

주어진 양의 정수를 이진수로 변환한 후, 그 이진수를 뒤집어 정수로 다시 변환한 결과를 출력하는 프로그램을 작성하세요.

- **입력**: 하나의 양의 정수 N이 주어집니다.
- **출력**: 이진수를 뒤집어 변환한 결과 정수를 출력합니다.

#### 예시 입력/출력

```python
# 예시 입력 1
13

# 예시 출력 1
11

# 예시 입력 2
4

# 예시 출력 2
1
```

#### 입출력 설명

- 예시 1에서 13의 이진수 표현은 `1101`이고, 이를 뒤집으면 `1011`이 되어 10진수로 11입니다.
- 예시 2에서 4의 이진수 표현은 `100`이고, 이를 뒤집으면 `001`이 되어 10진수로 1입니다.


## 답
```
def reverse_binary(n):
    binary_stack = []
    while n > 0:
        remainder = n % 2
        binary_stack.append(str(remainder))
        n //= 2
    binary = ""
    while binary_stack:
        binary += binary_stack.pop()
    
    result = 0
    reversed_binary = binary[::-1]

    for i in range(len(binary)):
        result += int(binary[i]) * (2**i)
    return result
```
