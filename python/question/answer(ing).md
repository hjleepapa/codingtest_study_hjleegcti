
# 시간복잡도 분석 해설

## 문제 1
```python
def example_function_1(n):
    for i in range(n):
        print(i)
# 예제: example_function_1(5)
# for 루프:
# - range(5) => 0, 1, 2, 3, 4
# - 루프가 5번 실행되며, 각 반복마다 i 값이 출력됩니다.
#   출력: 0, 1, 2, 3, 4

# example_function_1(5)를 호출하면 출력은 다음과 같습니다:
# 0
# 1
# 2
# 3
# 4

# 총 반복 횟수 및 print 호출 횟수:
# - for 루프: 5번 (i = 0, 1, 2, 3, 4)
```
### 해설
이 함수는 `n` 번의 반복을 수행합니다. 루프 내에서 수행되는 `print` 문은 상수 시간 복잡도를 가지며, 루프가 `n` 번 반복되므로 전체 시간 복잡도는 **O(n)** 입니다.

## 문제 2
```python
def example_function_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
# 예제: example_function_2(3)
# 첫 번째 for 루프 (i):
# - range(3) => 0, 1, 2
# 두 번째 for 루프 (j):
# - 각 i 값에 대해 range(3) => 0, 1, 2
# - 따라서 i가 0일 때 j는 0, 1, 2를 출력
# - i가 1일 때 j는 0, 1, 2를 출력
# - i가 2일 때 j는 0, 1, 2를 출력

# example_function_2(3)를 호출하면 출력은 다음과 같습니다:
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# 총 반복 횟수 및 print 호출 횟수:
# - 첫 번째 루프: 3번 (i = 0, 1, 2)
# - 두 번째 루프: 각 i에 대해 3번 (j = 0, 1, 2)
# - 전체 합계: 3 * 3 = 9번
```
### 해설
이 함수는 이중 루프를 가지고 있습니다. 외부 루프와 내부 루프 각각 `n` 번씩 반복되므로, 전체적으로 `n * n = n^2` 번의 반복이 일어납니다. 따라서 이 함수의 시간 복잡도는 **O(n^2)** 입니다.

## 문제 3
```python
def example_function_3(n):
    for i in range(n):
        print(i)
    for j in range(10):
        print(j)
# 예제: example_function_3(5)
# 첫 번째 for 루프:
# - range(5) => 0, 1, 2, 3, 4
# - 루프가 5번 실행되며, 각 반복마다 i 값이 출력됩니다.
#   출력: 0, 1, 2, 3, 4
# 두 번째 for 루프:
# - range(10) => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# - 루프가 10번 실행되며, 각 반복마다 j 값이 출력됩니다.
#   출력: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# example_function_3(5)를 호출하면 출력은 다음과 같습니다:
# 0
# 1
# 2
# 3
# 4
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# 총 반복 횟수 및 print 호출 횟수:
# - 첫 번째 루프: 5번 (i = 0, 1, 2, 3, 4)
# - 두 번째 루프: 10번 (j = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# - 전체 합계: 15번
```
### 해설
이 함수는 두 개의 루프를 가지고 있습니다. 첫 번째 루프는 `n` 번 반복되고, 두 번째 루프는 상수 시간인 10번 반복됩니다. 두 루프의 시간 복잡도를 각각 계산하면 첫 번째 루프는 **O(n)**, 두 번째 루프는 **O(1)** 입니다. 전체 시간 복잡도는 가장 높은 차수에 의해 결정되므로 **O(n)** 입니다.

## 문제 4
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Example: fibonacci(5)
# Call trace for fibonacci(5):
# fibonacci(5)
# ├─ fibonacci(4)
# │  ├─ fibonacci(3)
# │  │  ├─ fibonacci(2)
# │  │  │  ├─ fibonacci(1) => 1  (1 call)
# │  │  │  └─ fibonacci(0) => 0  (1 call)
# │  │  └─ Result of fibonacci(2) = 1 + 0 = 1  (2 calls)
# │  │  ├─ fibonacci(1) => 1  (1 call)
# │  │  └─ Result of fibonacci(3) = 1 + 1 = 2  (5 calls)
# │  ├─ fibonacci(2)
# │  │  ├─ fibonacci(1) => 1  (1 call)
# │  │  └─ fibonacci(0) => 0  (1 call)
# │  │  └─ Result of fibonacci(2) = 1 + 0 = 1  (2 calls)
# │  └─ Result of fibonacci(4) = 2 + 1 = 3  (9 calls)
# ├─ fibonacci(3)
# │  ├─ fibonacci(2)
# │  │  ├─ fibonacci(1) => 1  (1 call)
# │  │  └─ fibonacci(0) => 0  (1 call)
# │  │  └─ Result of fibonacci(2) = 1 + 0 = 1  (2 calls)
# │  ├─ fibonacci(1) => 1  (1 call)
# │  └─ Result of fibonacci(3) = 1 + 1 = 2  (5 calls)
# └─ Result of fibonacci(5) = 3 + 2 = 5  (15 calls)

# Total number of calls: 15
```
### 해설
이 함수는 재귀적으로 피보나치 수를 계산합니다. 이 재귀 함수의 시간 복잡도는 피보나치 수열의 특성상 **O(2^n)** 으로, 이는 각 함수 호출이 두 개의 새로운 호출을 생성하기 때문에 발생합니다. 이러한 지수적 증가로 인해, 이 알고리즘의 시간 복잡도는 **O(2^n)** 입니다.

## 문제 5
```python
def example_function_5(n):
    i = n
    while i > 1:
        i = i // 2
        print(i)
# Example: example_function_5(5)
# Initial value of i: 5
# First iteration:
# - i = 5 // 2 = 2
# - print(2) => Output: 2
# Second iteration:
# - i = 2 // 2 = 1
# - print(1) => Output: 1
# Loop ends as i is now 1, which is not greater than 1.

# The output when calling example_function_5(5) will be:
# 2
# 1

# Total number of iterations (and print calls): 2
```
### 해설
이 함수는 `i`를 2로 나누는 과정을 반복하며, 이는 `i`가 1 이하가 될 때까지 계속됩니다. 이 과정에서 루프의 반복 횟수는 `n`이 2로 나누어지는 횟수와 동일하며, 이는 `log_2(n)` 에 해당합니다. 따라서 이 함수의 시간 복잡도는 **O(log n)** 입니다.
