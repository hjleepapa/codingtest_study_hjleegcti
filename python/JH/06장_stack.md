# 목차

1. [질문](https://www.notion.so/Stack-65b25bcc041445018f57a6ddc93c7372?pvs=21)
2. [실전 문제](https://www.notion.so/Stack-65b25bcc041445018f57a6ddc93c7372?pvs=21)

---

## 질문

1. 스택을 이용하여 주어진 문자열을 뒤집는 알고리즘을 설계하고 구현해 보세요. 이 알고리즘의 시간 복잡도와 공간 복잡도는 각각 어떻게 되나요? 스택을 사용하지 않고도 문자열을 뒤집을 수 있는 다른 방법을 설명해 보세요.

```bash
// using stack 
// space complexity : O(N) 
// time complexity : O(N)

Algorithm reversed_string_with_stack(string:str)
  string <- given
  stack = empty stack
  ret = ''
  n = sizeOf(string)
  for i = 0...n-1:
    stack.push(string[i])
  while ret is empty
    ret = ret + stack.top(); // concatenate 
	stack.pop();

// without using stack
// space complexity : O(N) <- string size 
# time complexity : O(N/2) ~ O(N) 

Algorithm reversed_string_without_stack(string:str)
  string <- given 
  n <- lengthOfStringSize
  L <- empty String
  R <- empty String
  m <- n//2 
  t  <- m if n % 2 == 1 else m - 1 

  for i=0...m-1:
    L += string[t-i]
    R += string[n-1-i]

  if t == m 
    L += string[0]

  return R + L

   
```

## - Implementation by python

```python
# implementation 1 
# with stack

def reversed_string(str1:str):	
    st = []
    ret = '' # return string 

    for string in str1: # O(N) : N, string length
        st.append(string) 

    while st:  # O(N)
        ret += st.pop()

    return ret 

a = reversed_string('abc')

def reversed_string_without_stack(str1:str):
    
    n = len(str1)
    L = ''
    R = ''
    m = n//2  # 0 1 2 3 4 
    t = m - 1 if n % 2 == 0 else m  

    for i in range(m): # O(N/2) 
        L += str1[t-i] # 2 1 0
        R += str1[n-1-i]  

    if n % 2 == 1 :
        L += str1[0] 

    return R + L

print(a) # cba 
print(reversed_string_without_stack('12345')) # 54321
print(reversed_string_without_stack('543210')) # 012345
```

- 두 경우 시간/공간복잡도는 전부 O(n)

2. 스택이 재귀적인 함수 호출과 어떻게 관련이 있는지 설명해 보세요. 재귀 함수를 스택을 사용하여 비재귀적으로 변환하는 방법을 예시를 통해 설명할 수 있나요?

---

재귀함수의 base case를 호출하는 것과 스택의 LIFO(Last In, First Out)과 관련되어 있습니다. 

재귀함수는 점화식을 이용하는 함수입니다. 그러기 위해서는 반드시 base case가 존재해야 합니다. 

그렇지 않으면, 재귀함수는 영원히 돕니다. 

이 base case는 stack의 LIFO과 유사합니다. base case가 제일 늦게 등장하지만, 제일 빨리 return이 되기 때문입니다. 아래 fibonacci 를 재귀함수로 구현한 것과 비재귀로 구현한 것을 비교해보겠습니다. 

```python

def fibo(n:int): # fibonacci 재귀 O(2^n)
    if n<=1:
        return 1 
    return fibo(n-1) + fibo(n-2)

def fibo1_using_stack(n:int): # fibonacci 비재귀 + memoization O(N)

    stack = [] 
    memo = [1,1] + [0] * n 
    ret = 0
    stack.append(n)

    while stack:
        cur = stack.pop()
        if memo[cur]:
            ret += memo[cur]
            continue
        else:
            if memo[cur-1] == 0:
                stack.append(cur-1)
            else:
                ret += memo[cur-1]
            
            if memo[cur-2] == 0:
                stack.append(cur-2)
            else:
                ret += memo[cur-2]

            if memo[cur-1] * memo[cur-2] > 0:    
                memo[cur] = memo[cur-1] + memo[cur-2]
    return ret 

print(fibo1_using_stack(20))
```

재귀함수의 코드를 보면 피보나치 구조에서 제일 아래인 n ≤ 1인 경우 값을 return 하는 것을 알 수 있습니다. 스택으로 구현한 비재귀 피보나치도 마찬가지로 제일 말단인 cur ≤ 1가 되는 경우 ret에 값을 더해주는 걸 알 수 있습니다. 

이를 좀 더 빠르게 생략하기 위해 memoization 스타일로 구현했습니다. → else 다음에  

else: 

  stack.append(cur-1)

  stack.append(cur-2) 만 적힌 것이 본래 코드입니다. 

## 실전 문제

### 문제 1: HTML 태그 유효성 검사

HTML 문서에서 태그가 올바르게 열리고 닫혔는지 확인하는 프로그램을 작성하세요. `<tag>` 형태로 열리고 `</tag>` 형태로 닫혀야 합니다. 태그 이름은 영문 소문자만 사용됩니다.

- **입력**: HTML 태그가 포함된 문자열이 주어집니다.
- **출력**: 태그가 올바르게 열리고 닫혔다면 `True`, 그렇지 않다면 `False`를 출력합니다.

### 예시 입력/출력

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

### 입출력 설명

- 예시 1에서는 `<div>` 태그가 `<p>` 태그를 포함하고, 올바르게 닫히므로 `True`를 반환합니다.
- 예시 2에서는 `<span>` 태그가 `<div>` 태그 내에서 닫히기 때문에 구조가 올바르지 않아 `False`를 반환합니다.

### 문제 1. 풀이

이것은 프로그래머스에 올바른 괄호 문제랑 비슷합니다. 

<tag>의 tag를 전부 stack에 넣는다. 그후 나오는 닫는 태그는 </를 체크하면서 확인할 수 있습니다.

```python
def html_right_tag(html_source:str): # O(N)
    st = []
    idx = 0
    n = len(html_source)
 
    while idx < n: 
        
        if html_source[idx] == '<':
            tmp = ''
            while html_source[idx+1] != '>':
                tmp += html_source[idx+1]
                idx+=1 
            if tmp[0] == '/':
                if st and st[-1] == tmp[1:]:
                    st.pop()
                else:
                    return False
            else:
                st.append(tmp)
        else:
            idx+=1 
            continue
    
    return True
    
print(html_right_tag("<p>a</p>"))	# True
url2 = "<div><td><p>Hello</p></td></div>"
print(html_right_tag(url2)) # True
```

### 문제 2: 역순 이진수 표현

주어진 양의 정수를 이진수로 변환한 후, 그 이진수를 뒤집어 정수로 다시 변환한 결과를 출력하는 프로그램을 작성하세요.

- **입력**: 하나의 양의 정수 N이 주어집니다.
- **출력**: 이진수를 뒤집어 변환한 결과 정수를 출력합니다.

### 예시 입력/출력

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

### 입출력 설명

- 예시 1에서 13의 이진수 표현은 `1101`이고, 이를 뒤집으면 `1011`이 되어 10진수로 11입니다.
- 예시 2에서 4의 이진수 표현은 `100`이고, 이를 뒤집으면 `001`이 되어 10진수로 1입니다.

### 문제 2. 풀이

질문 1에 나온 것처럼 스택을 이용해서 구한 이진수를 뒤집어봅시다.

주어진 숫자를 0이 될 때까지 2로 나누면서, 나머지를 스택에 넣습니다. 

그 다음에는 join을 이용해서 하나의 str으로 만들었습니다.  

```python
# O(N) 

def num_to_reversed_binary(num:int):
	st = []
	while num:
		num, r = num//2, num % 2 
		st.append(str(r))
	
	return int(''.join(st), 2) 

print(num_to_reversed_binary(13))
```
