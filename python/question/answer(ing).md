# 시간 복잡도실제 예시

## O(1) - 상수 시간 복잡도

### 예제
```python
def get_first_element(arr):
    return arr[0]
```

### 설명
이 함수의 시간 복잡도는 O(1)입니다. 왜냐하면 배열의 크기와 상관없이 첫 번째 요소를 반환하는 데 걸리는 시간은 동일하기 때문입니다. `arr`가 얼마나 크든 상관없이, `arr[0]` 연산은 일정한 시간 내에 수행됩니다.

## O(logN) - 로그 시간 복잡도

### 예제
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### 설명
이진 탐색 알고리즘의 시간 복잡도는 O(logN)입니다. 배열의 크기가 증가할수록 탐색해야 할 범위가 절반으로 줄어들기 때문에, N개의 요소가 있을 때 최대 로그(log) N 단계만큼의 비교가 필요합니다. 따라서 시간 복잡도는 O(logN)입니다.

## O(N) - 선형 시간 복잡도

### 예제
```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

### 설명
이 함수의 시간 복잡도는 O(N)입니다. 배열의 모든 요소를 하나씩 합산해야 하므로, 배열의 크기 N에 비례하여 수행 시간이 증가합니다. N개의 요소를 포함하는 배열에서는 N번의 덧셈 연산이 필요하기 때문에 시간 복잡도는 O(N)입니다.

## O(NlogN) - 선형 로그 시간 복잡도

### 예제
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### 설명
병합 정렬 알고리즘의 시간 복잡도는 O(NlogN)입니다. 병합 정렬은 배열을 재귀적으로 반씩 나누어 정렬한 후 병합합니다. 배열을 나누는 단계는 로그(log) N 단계가 필요하며, 각 단계에서 N개의 요소를 정렬하고 병합합니다. 따라서 전체 시간 복잡도는 O(NlogN)입니다.

## O(N^2) - 이차 시간 복잡도

### 예제
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### 설명
버블 정렬 알고리즘의 시간 복잡도는 O(N^2)입니다. 이 알고리즘은 배열의 각 요소를 반복적으로 비교하고 교환하며 정렬합니다. 두 개의 중첩된 반복문이 있어, 첫 번째 반복문이 N번 실행될 때마다 두 번째 반복문이 N-i-1번 실행됩니다. 결과적으로, 최악의 경우 N * (N-1)/2번의 비교가 필요하며, 이는 O(N^2)에 해당합니다.

## O(2^N) - 지수 시간 복잡도

### 예제
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

### 설명
이 재귀적 피보나치 함수의 시간 복잡도는 O(2^N)입니다. 각 호출에서 두 개의 하위 문제를 생성하고, 그 각각은 다시 두 개의 하위 문제를 생성하는 방식으로 계산이 진행됩니다. 이러한 재귀적 호출은 지수적으로 증가하여, 입력 크기 N에 대해 2^N개의 호출이 필요하게 됩니다. 따라서 이 알고리즘의 시간 복잡도는 O(2^N)입니다.

## 시간 복잡도별 연산 횟수 비교

아래 표는 N의 값이 10, 100, 3000, 5000, 10000일 때 각 시간 복잡도에 따른 연산 횟수를 비교한 것입니다.

|   N   |  O(1)  |  O(logN)  |  O(N)  |  O(NlogN)  |  O(N^2)   |  O(2^N)   |
|:-----:|:------:|:---------:|:------:|:----------:|:---------:|:---------:|
|  10   |   1    |   3.32    |   10   |   33.22    |    100    |   1024    |
|  100  |   1    |   6.64    |  100   |   664.39   |   10000   | 계산 불가 |
| 3000  |   1    |   11.55   |  3000  |  34652.2   |  9000000  | 계산 불가 |
| 5000  |   1    |   12.29   |  5000  |  61438.6   | 25000000  | 계산 불가 |
| 10000 |   1    |   13.29   | 10000  |   132877   | 100000000 | 계산 불가 |


# 시간복잡도 문제
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
