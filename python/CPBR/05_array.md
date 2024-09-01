
## 기본 배열 질문

1. **파이썬에서 리스트의 장점 및 단점에 대해 말해주세요. 단점이 있다면 이를 해결할 수 있는 방법은 무엇이 있을까요?** 
    
- 장점 : 리스트는 한 개의 리스트에 혼합하여 다양한 자료구조를 포함할 수 있으며 확장이 쉽다. 또한 숫자나 문자열 등의 변수를 선언하지 않고도 간단하게 표현할 수 있다. 
    
- 단점 : 파이썬에서는 리스트도 객체에 해당하기 때문에 복사를 하게되면 바로보는 객체가 동일하기 때문에 두 개의 리스트 중 하나만 변경해도 나머지 하나가 동일하게 수정되는 현상이 발생한다.
  - 예를 들어 a라는 변수를 선언하고 리스트를 만들어 a에 할당하면 리스트 객체의 주소가 저장된 변수가 된다. 그럼 a라는 변수의 값을 b 인자에 할당하였을 경우, b는 a와 같은 객체의 주소가 저장된 변수가 된다. 따라서 b를 불러와 인덱스 2번의 값을 5로 변경하면, a에도 똑같이 적용된다.
    ```python
     b = a
    print(b)
    b[2] = 5
    print(b)
    print(a)

    #결과값
    [1, 2, 3, 4]
    [1, 2, 5, 4]
    [1, 2, 5, 4]
    ``` 
    <br>
**2. 일반적인 배열과  파이썬 리스트의 차이점은 무엇인가요?**
    
- 일반적인 배열의 크기는 고정되어 있다. 하지만 파이썬 리스트는 동적으로 크기를 조정할 수 있다.
- 일반적인 배열은 동일한 데이터 유형의 요소들로 구성되어 있어야 한다. 하지만 파이썬 리스트는 다양한 데이터 유형을 혼합하여 가질 수 있다.<br>
    
**3. 정렬된 두 개의 리스트를 하나의 정렬된 리스트로 만드는 방법이 있을까요? 있다면 로직을 설명하시고 시간복잡도 측면에서도 설명해주세요.**

- 리스트를 연결 후 정렬 :
  이 경우 두 리스트를 합친 크기가 2n이므로 시간 복잡도는 **O(n log n)**
- 정렬된 리스트를 병합 :
  두 리스트 a 와 b의 첫 요소부터 크기를 비교하며 작은 요소를 result 에 삽입한다. 두 리스트는 이미 정렬된 형태임을 활용하여 비교와 병합만으로 작업을 완료한다.
  - 리스트 a와 b의 길이를 각각 n이라고 가정하면, 두 리스트를 병합하는 과정에서 각 요소를 한 번씩만 비교하고 결과 리스트에 추가
  - 이 경우 병합 과정의 시간 복잡도는 **O(n)**<br>
    
**4. 정렬된 리스트와 정렬되지 않은 리스트에서 특정 원소를 탐색하는 방법에 대해 설명하고, 각 경우의 시간 복잡도에 대해 논해주세요.**
   - 위와 같으며 이미 정렬된 리스트를 추가적으로 정렬하는 것은 비효율적이기 때문에, 단순히 리스트를 연결한 후 sort()를 호출하는 방법(O(n log n))은 낭비가 될 수 있음
   - 정렬된 상태를 이용하여 직접 병합하는 방법을 사용한다면 시간복잡도는 **O(n)** <br>

**5. 파이썬에서 문자열을 순회하면서, 'abcde'에서 'bcdea', 'cdeab'처럼 앞뒤가 연결된 형태로 출력하려고 합니다. 리스트의 인덱스를 넘어설 때마다 이러한 순회를 효율적으로 구현하려면, 인덱스 계산을 어떻게 해야 할까요?**
    
  - 모듈러 연산(%)을 활용한다
  ```python
  n = len('abcde')
for i in range(n) : 
    answer = ''.join('abcde'[(i + j) % n] for j in range(n))
    print (answer)
  ```
---

## 리스트의 합 문제

- **문제 설명**: 주어진 정수 리스트에서 두 수의 합이 특정 목표 값이 되는 모든 쌍을 찾아라.
- **입력**: 정수 리스트와 목표 정수
- **출력**: 목표 값이 되는 모든 수 쌍 (중복 없이)

**예시 (Python)**

```python
nums = [2, 7, 11, 15]
target = 9
# 출력: [(2, 7)]
```
**작성한 정답**
```python
def solution(nums, target):
    pairs = []
    length = len(nums)
    
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    
    return pairs
```
---

## 연속된 1의 최대 길이

- **문제 설명**: 0과 1로 이루어진 리스트에서 가장 긴 연속된 1의 길이를 찾아라.
- **입력**: 0과 1로만 이루어진 리스트
- **출력**: 가장 긴 연속된 1의 길이

**예시 (Python)**

```python
nums = [1, 1, 0, 1, 1, 1]
# 출력: 3
```
**작성한 정답**
```python
def solution (nums):
    max_length = 0
    current_length = 0
    
    for num in nums:
        if num == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
    
    # 마지막 연속된 1의 길이 처리
    max_length = max(max_length, current_length)
    
    return max_length
```
---

## 중복 요소 찾기

- **문제 설명**: 정수 리스트에서 중복된 숫자를 모두 찾아라.
- **입력**: 정수 리스트
- **출력**: 중복된 숫자의 리스트

**예시 (Python)**

```python
nums = [4, 3, 2, 7, 8, 2, 3, 1]
# 출력: [2, 3]
```
**작성한 정답**
```python
def solution (nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)
```

---

## 회전된 리스트의 회전 횟수 찾기

- **문제 설명**: 주어진 리스트가 몇 번 회전되어 오름차순으로 정렬될 수 있는지 찾는 문제입니다. 원래 리스트는 오름차순으로 정렬된 상태에서 오른쪽으로 회전된 상태입니다.
- **입력**: 정렬된 리스트가 오른쪽으로 회전된 상태의 리스트
- **출력**: 리스트가 오름차순으로 정렬되기 위해 필요한 회전 횟수

**예시 (Python)**

```python
nums = [4, 5, 6, 7, 0, 1, 2]
# 출력: 4
```
**작성한 정답**
```python
def find_rotation_count(nums):
    # 리스트에서 가장 작은 값의 인덱스를 찾는다
    min_index = nums.index(min(nums))
    return min_index
```
---

## 2D 리스트의 나선형 출력

- **문제 설명**: N x N 크기의 2D 리스트를 나선형(spiral) 순서로 출력하라.
- **입력**: N x N 2D 리스트
- **출력**: 나선형 순서로 배열된 요소들의 리스트

**예시 (Python)**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 출력: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
**작성한 정답**
```python
def solution (matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # 오른쪽으로 이동
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # 아래로 이동
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # 왼쪽으로 이동
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # 위로 이동
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```
---

## 리스트에서 모듈러 연산 문제

- **문제 설명**: 주어진 리스트에서 각 요소를 k로 나눈 나머지를 계산하여 나머지가 같은 요소들이 몇 개 있는지 세어라.
- **입력**: 정수 리스트와 나눌 수 k
- **출력**: 나머지가 같은 요소들의 개수

**예시 (Python)**

```python
nums = [2, 3, 5, 8, 10, 14]
k = 3
# 출력: [(2, 1), (0, 2), (1, 3)]  
# 나머지가 2인 요소는 1개, 나머지가 0인 요소는 2개, 나머지가 1인 요소는 3개
```
**작성한 정답**
```python
def count_mod(nums, k):
    mods = []
    for num in nums:
        mod = num % k
        mods.append(mod)
        
    counter = set(mods)
    pairs = []
    for c in counter:
        pairs.append((c, mods.count(c)))
    print(pairs)
    
    
nums = [2, 3, 5, 8, 10, 14]
k = 3
count_mod(nums, k)
```

---

## 슬라이딩 윈도우 최대합 문제

- **문제 설명**: 길이가 N인 정수 리스트에서 연속된 K개의 요소로 이루어진 부분 리스트의 최대 합을 찾아라.
- **입력**: 정수 리스트와 정수 K
- **출력**: 연속된 K개의 요소의 최대 합

**예시 (Python)**

```python
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
# 출력: 39  # 부분 리스트 [4, 2, 10, 23]의 합이 39로 최대
```
**작성한 정답**
```python
def max_sum_subarray(nums, k):
    # 유효성 검사: 리스트가 비어있거나 k가 유효하지 않은 경우
    if not nums or k <= 0 or k > len(nums):
        return 0

    # 초기 윈도우 합 계산
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # 슬라이딩 윈도우
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```
---

## 특정 좌표의 8방향 값 출력 문제

- **문제 설명**: 주어진 2D 리스트에서 특정 좌표 (x, y)의 주변 8방향 값을 출력하라. 만약 범위를 벗어나는 경우, "벗어났다"라는 메시지를 출력해야 한다.
- **입력**: N x M 2D 리스트, 좌표 (x, y)
- **출력**: 특정 좌표의 8방향 값 또는 범위를 벗어난 경우 "벗어났다" 메시지 출력

**예시 (Python)**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
x = 1
y = 1
# 출력: 1, 2, 3, 4, 6, 7, 8, 9  (모두 범위 내에 있음)
```
**작성한 정답**
```python
def solution(matrix, x, y):
  
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    if not (0 <= x < rows and 0 <= y < cols):
        return "벗어났다"
    
    # 8방향 좌표 정의 (상, 하, 좌, 우, 대각선)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # 상좌, 상중, 상우
        (0, -1),          (0, 1),    # 좌, 우
        (1, -1), (1, 0), (1, 1)      # 하좌, 하중, 하우
    ]
    
    surrounding_values = [
        matrix[x + dx][y + dy]
        for dx, dy in directions
        if 0 <= x + dx < rows and 0 <= y + dy < cols
    ]
    
    return surrounding_values
```
---

## 지뢰 찾기 의사코드 작성 문제

- **문제 설명**: 지뢰 찾기 게임에서 지뢰의 위치가 주어졌을 때, 각 빈 칸이 주변에 몇 개의 지뢰가 있는지 계산하는 로직을 의사코드로 작성하라.
- **입력**: N x M 크기의 2D 리스트, 지뢰의 위치가 표시된 리스트
- **출력**: 각 빈 칸의 지뢰 개수를 계산한 결과 리스트

**예시 (Pseudo-Code)**

```
Input: 
matrix = [
  ['M', '.', '.', 'M'],
  ['.', '.', '.', '.'],
  ['.', 'M', '.', '.']
]

Output:
[
  ['M', 2, 1, 'M'],
  [2, 3, 2, 1],
  [1, 'M', 1, 0]
]
```
```python
주어진 2D 리스트를 입력으로 받아, 지뢰는 특정 기호로 표시하고, 빈 칸은 다른 기호로 표시한다. 먼저 행렬의 크기를 구하고, 같은 크기의 결과 행렬을 초기화한다. 이 결과 행렬은 각 빈 칸 주변의 지뢰 개수를 저장한다.
8개의 방향을 정의한다. 상하좌우와 대각선 방향을 포함하여 총 8개 방향을 설정한다. 이후, 행렬의 모든 셀을 순회하면서 지뢰가 있는지 확인한다. 각 셀을 방문할 때, 만약 지뢰라면 결과 행렬의 해당 위치에도 지뢰를 저장한다. 빈 칸인 경우에는 주변 지뢰 개수를 세기 위해 카운트를 0으로 초기화한다.
각 방향에 대해 현재 셀의 좌표에 방향의 변화를 더해 인접한 셀의 좌표를 계산한다. 이때 인접한 좌표가 유효한 범위에 있는지 확인하고, 범위를 벗어나면 무시한다. 유효한 좌표가 지뢰라면 카운트를 1 증가시킨다. 모든 방향을 확인한 후, 계산된 카운트를 결과 행렬의 현재 빈 칸 위치에 저장한다.
이 과정을 모든 셀에 대해 반복한 뒤, 완성된 결과 행렬을 반환한다. 이렇게 하면 각 빈 칸 주변의 지뢰 개수를 효율적으로 계산할 수 있다.
```

---
