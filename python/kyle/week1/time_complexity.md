# 시간복잡도 계산 문제

## 문제 1
다음 코드의 시간복잡도를 빅오 표기법으로 나타내세요.
```python
def example_function_1(n):
    for i in range(n):
        print(i)
```

##  문제 1 답
```
N=1 일 때 실행횟수는 1
N=2 일 때 실행횟수는 2
...
N=x 일 때 실행횟수는 x
시간복잡도는 O(n)
```

## 문제 2
다음 코드의 시간복잡도를 분석하고 빅오 표기법으로 표현하세요.
```python
def example_function_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

## 문제2 답
```
- range(n)함수는 0부터 n-1까지의 정수 range 객체를 반환하며, 리스트와 튜플로 형변환할 수 있음. 반복문에서는 iterator로 사용됨
N=1일 때 range(1)은 0, 첫 번째 반복문의 실행횟수 1, 두번째 반복문의 실행횟수 1, 총 1*1 1회
N=2일 때 range(2)은 0~1, 첫 번째 반복문의 실행횟수 2, 두번째 반복문의 실행횟수 2, 총 2*2 4회
N=3일 때 range(3)은 0~2, 첫 번쨰 반복문의 실행횟수 3, 두번째 반복문의 실행횟수 3, 총 3*3 9회
N=5일 때 range(5)은 0~4, 첫 번째 반복문의 실행횟수 5, 두번째 반복문의 실행횟수 5, 총 5*5 25회
...
N=x일 때 range(x)는 0~x-1, 첫 번째 반복문의 실행횟수 x, 두 번째 반복문의 실행회숫 x, 총 x*x = x^2회

따라서 시간복잡도는 O(n^2)
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

## 문제 3 답
```
시간 복잡도는 최고차항이 결정하므로, 상수 10만큼 반복하는 두 번째 반복문은 고려하지 않음
첫 번째 반복문의 인자인 n이 결정하며, range(n)은 0~n-1까지 총 n개의 인자를 순서대로 반환하며 반복문을 실행할 것이므로

시간복잡도는 O(n)
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

## 문제 4 답
```
조건문을 if-else로 구현한 경우, if의 조건을 부합하면 else는 실행하지 않음.
따라서 fibonacci(n)은 어떤 경우에든 1회 실행되고 종료함.
                                        fib(5)
                        fib(4)                          fib(3)
                fib(3)          fib(2)          fib(2)          fib(1)
            fib(2) fib(1)   fib(1) fib(0)    fib(1) fib(0)
        fib(1)fib(0)

2회씩 분열하므로 가장 긴 경우
최대 시간복잡도는 O(2^n)
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

## 문제 5 답
```
i = 16이면 실행 횟수는 8->4->2->1으로 4회 실행
i = 32이면 실행 횟수는 16->8->4->2->1로 5회 실행
i = 2^n이면 실행 횟수는  n회 실행

i = O(x)이면 실행 횟수는 x =2^n, 이므로 log2x = n -> log2x회 실행

따라서 최대 시간복잡도는 O(logn)
```
