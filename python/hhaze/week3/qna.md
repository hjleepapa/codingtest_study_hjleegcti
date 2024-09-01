# 기본 배열 질문
1. 파이썬에서 리스트의 장점 및 단점에 대해 말해주세요. 단점이 있다면 이를 해결할 수 있는 방법은 무엇이 있을까요?
- 장점
  - 동적으로 크기 조절할 수 있도록 구현되어 있어 다른 언어의 배열 기능을 그대로 사용할 수 있으면서 배열 크기도 가변적
  - 슬라이싱, 삽입, 삭제, 연결 등의 연산을 제공하므로 더 편리
  - 임의 접근이라는 특징이 있어 데이터에 인덱스로 바로 접근할 수 있어 데이터에 빈번하게 접근하는 경우 효율적
- 단점
  - 메모리 공간을 충분히 확보해야 한다는 점
  - 중간에 요소를 삽입하거나 삭제하는 경우 해당 위치 이후의 모든 요소를 이동시켜야 한다는 점
- 단점 해결 방법
  - 리스트의 중간 삽입이나 삭제가 빈번하게 일어나는 경우 `collections.deque` 사용 -> `deque`는 양쪽 끝에서 삽입과 삭제가 O(1)의 시간 복잡도로 매우 효율적

2. 일반적인 배열과 파이썬 리스트의 차이점은 무엇인가요?
- 크기 조절
  - 일반적인 배열은 고정된 크기를 가지며 한 번 크기가 정해지면 변경 불가
  - 파이썬 리스트는 동적으로 크기를 조절할 수 있도록 구현되어 있어 요소를 추가하거나 삭제할 때 자동으로 크기 조정
- 데이터 타입
  - 일반적인 배열은 모든 요소가 동일한 데이터 타입
  - 파이썬 리스트는 다양한 데이터 타입을 혼합해서 저장 가능

3. 정렬된 두 개의 리스트를 하나의 정렬된 리스트로 만드는 방법이 있을까요? 있다면 로직을 설명하시고 시간복잡도 측면에서도 설명해주세요.
```python
def solution(arr1, arr2):
    arr1 = arr1 + arr2
    arr1.sort()

    return arr1
```
- 시간 복잡도는 O(NlogN)
  - `+` 연산자로 리스트 맨 끝에 다른 리스트의 데이터를 추가하는 부분은 O(1)의 시간 복잡도이고, `sort()` 메서드는 O(NlogN) 시간 복잡도

4. 정렬된 리스트와 정렬되지 않은 리스트에서 특정 원소를 탐색하는 방법에 대해 설명하고, 각 경우의 시간 복잡도에 대해 논해주세요.
- 정렬된 리스트
  - 이진 탐색 알고리즘 사용 가능
    - 리스트의 중간 원소를 확인하고 찾고자 하는 값이 중간 원소보다 큰지 작은지에 따라 리스트의 절반만 탐색하는 과정을 반복
  - 시간 복잡도 O(logN)
- 정렬되지 않은 리스트
  - 리스트의 각 요소를 차례대로 확인하면서 원하는 원소가 있는지 확인
  - 시간 복잡도 O(N)

5. 파이썬에서 문자열을 순회하면서, 'abcde'에서 'bcdea', 'cdeab'처럼 앞뒤가 연결된 형태로 출력하려고 합니다. 리스트의 인덱스를 넘어설 때마다 이러한 순회를 효율적으로 구현하려면, 인덱스 계산을 어떻게 해야 할까요?
```python
def solution(s):
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        print(rotated)
```

# 리스트의 합 문제
- 문제 설명: 주어진 정수 리스트에서 두 수의 합이 특정 목표 값이 되는 모든 쌍을 찾아라.
- 입력: 정수 리스트와 목표 정수
- 출력: 목표 값이 되는 모든 수 쌍 (중복 없이)

예시 (Python)
```python
nums = [2, 7, 11, 15]
target = 9
# 출력: [(2, 7)]
```

```python
def solution(arr, target):
    answer = []
    
    n = len(arr)
    arr.sort()
    start = 0
    end = n - 1

    while start < end:
        sum = arr[start] + arr[end]

        if sum == target:
            answer.append((arr[start], arr[end]))
            start += 1
            end -= 1
        elif sum > target:
            end -= 1
        else:
            start += 1

    return answer
```

# 연속된 1의 최대 길이
- 문제 설명: 0과 1로 이루어진 리스트에서 가장 긴 연속된 1의 길이를 찾아라.
- 입력: 0과 1로만 이루어진 리스트
- 출력: 가장 긴 연속된 1의 길이

예시 (Python)
```python
nums = [1, 1, 0, 1, 1, 1]
# 출력: 3
```

```python
def solution(arr):
    count = 0
    max_count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
        
    return max(count, max_count)
```

# 중복 요소 찾기
- 문제 설명: 정수 리스트에서 중복된 숫자를 모두 찾아라.
- 입력: 정수 리스트
- 출력: 중복된 숫자의 리스트

예시 (Python)
```python
nums = [4, 3, 2, 7, 8, 2, 3, 1]
# 출력: [2, 3]
```

```python
def solution(nums):
    answer = []

    num_dict = dict(Counter(nums))
    
    for k, v in num_dict.items():
        if v > 1:
            answer.append(k)
    
    return answer
```

# 회전된 리스트의 회전 횟수 찾기
- 문제 설명: 주어진 리스트가 몇 번 회전되어 오름차순으로 정렬될 수 있는지 찾는 문제입니다. 원래 리스트는 오름차순으로 정렬된 상태에서 오른쪽으로 회전된 상태입니다.
- 입력: 정렬된 리스트가 오른쪽으로 회전된 상태의 리스트
- 출력: 리스트가 오름차순으로 정렬되기 위해 필요한 회전 횟수

예시 (Python)
```python
nums = [4, 5, 6, 7, 0, 1, 2]
# 출력: 4
```

```python
def solution(nums):
    sorted_nums = list(sorted(nums))
    idx = nums.index(sorted_nums[0])

    return idx
```

# 2D 리스트의 나선형 출력
- 문제 설명: N x N 크기의 2D 리스트를 나선형(spiral) 순서로 출력하라.
- 입력: N x N 2D 리스트
- 출력: 나선형 순서로 배열된 요소들의 리스트

예시 (Python)
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 출력: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

```python
def solution(matrix):
    result = []
    row_begin, row_end, col_begin, col_end = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for j in range(col_begin, col_end + 1):
            result.append(matrix[row_begin][j])
        row_begin += 1
        
        for i in range(row_begin, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for j in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][j])
        row_end -= 1
       
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
        col_begin += 1

    return result
```

# 리스트에서 모듈러 연산 문제
- 문제 설명: 주어진 리스트에서 각 요소를 k로 나눈 나머지를 계산하여 나머지가 같은 요소들이 몇 개 있는지 세어라.
- 입력: 정수 리스트와 나눌 수 k
- 출력: 나머지가 같은 요소들의 개수

예시 (Python)
```python
nums = [2, 3, 5, 8, 10, 14]
k = 3
# 출력: [(2, 1), (0, 2), (1, 3)]  
# 나머지가 2인 요소는 1개, 나머지가 0인 요소는 2개, 나머지가 1인 요소는 3개
```

```python
def solution(nums, k):
    num_dict = {}

    for num in nums:
        target = num % k
        print(num, target)

        if target in num_dict:
            num_dict[target] += 1
        else:
            num_dict[target] = 1
    
    return list(num_dict.items())
```

# 슬라이딩 윈도우 최대합 문제
- 문제 설명: 길이가 N인 정수 리스트에서 연속된 K개의 요소로 이루어진 부분 리스트의 최대 합을 찾아라.
- 입력: 정수 리스트와 정수 K
- 출력: 연속된 K개의 요소의 최대 합

예시 (Python)
```python
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
# 출력: 39  # 부분 리스트 [4, 2, 10, 23]의 합이 39로 최대
```

```python
def solution(nums, k):
    sub_sum = 0
    max_sum = 0

    for i in range(len(nums)):
        sub_list = nums[i:i + k]
        
        if len(sub_list) == k:
            sub_sum = sum(sub_list)
            max_sum = max(sub_sum, max_sum)
    
    return max_sum
```

# 특정 좌표의 8방향 값 출력 문제
- 문제 설명: 주어진 2D 리스트에서 특정 좌표 (x, y)의 주변 8방향 값을 출력하라. 만약 범위를 벗어나는 경우, "벗어났다"라는 메시지를 출력해야 한다.
- 입력: N x M 2D 리스트, 좌표 (x, y)
- 출력: 특정 좌표의 8방향 값 또는 범위를 벗어난 경우 "벗어났다" 메시지 출력

예시 (Python)
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

```python
def is_valid(nx, ny):
    return 0 <= nx < 3 and 0 <= ny < 3

def solution(matrix, x, y):
    target = []

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue                
            
            if is_valid(i, j):
                target.append(matrix[i][j])
            else:
                return '벗어났다'

    return ', '.join(map(str, target))
```

# 지뢰 찾기 의사코드 작성 문제
- 문제 설명: 지뢰 찾기 게임에서 지뢰의 위치가 주어졌을 때, 각 빈 칸이 주변에 몇 개의 지뢰가 있는지 계산하는 로직을 의사코드로 작성하라.
- 입력: N x M 크기의 2D 리스트, 지뢰의 위치가 표시된 리스트
- 출력: 각 빈 칸의 지뢰 개수를 계산한 결과 리스트

예시 (Pseudo-Code)
```python
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
def is_valid(nx, ny, N, M):
    return 0 <= nx < N and 0 <= ny < M

def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = [[0] * col for _ in range(row)]

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for x in range(row):
        for y in range(col):
            if matrix[x][y] == 'M':
                result[x][y] = 'M'
            else:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]

                    if is_valid(nx, ny, row, col):
                        if matrix[nx][ny] == 'M':
                            result[x][y] += 1

    return result
```