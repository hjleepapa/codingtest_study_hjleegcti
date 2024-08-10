# 시간복잡도 개념 질문
1. 시간복잡도가 무엇인지 정의하고, 왜 알고리즘의 성능을 평가할 때 중요한지 설명하세요.
2. 빅오 표기법이 무엇인지 설명하고, 알고리즘의 시간복잡도를 표현할 때 빅오 표기법이 사용되는 이유를 설명하세요.
3. 빅오 표기법에서 최악의 경우(worst-case)를 고려하는 이유는 무엇인가요? 실제 상황에서 최악의 경우 시간복잡도가 중요한 이유를 설명하세요.
4. 빅오 표기법을 사용하여 알고리즘의 효율성을 평가할 때 나타날 수 있는 한계점이나 오해는 무엇인지 설명하세요.


# 시간복잡도 계산 문제

## 문제 1
다음 코드의 시간복잡도를 빅오 표기법으로 나타내세요.
```python
def example_function_1(n):
    for i in range(n):
        print(i)
```

## 문제 2
다음 코드의 시간복잡도를 분석하고 빅오 표기법으로 표현하세요.
```python
def example_function_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

## 문제 3
다음 코드의 시간복잡도를 분석하고 빅오 표기법으로 표현하세요.
```python
def example_function_3(n):
    for i in range(n):
        print(i)
    for j in range(10):
        print(j)
```

## 문제 4
다음 코드의 시간복잡도를 분석하고 빅오 표기법으로 표현하세요.
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## 문제 5
다음 코드의 시간복잡도를 계산하고 빅오 표기법으로 나타내세요.
```python
def example_function_3(n):
    i = n
    while i > 1:
        i = i // 2
        print(i)
```
