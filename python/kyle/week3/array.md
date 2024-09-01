
## 기본 배열 질문

1. 파이썬에서 리스트의 장점 및 단점에 대해 말해주세요. 단점이 있다면 이를 해결할 수 있는 방법은 무엇이 있을까요?
- 장점
    - 리스트는 크기들 동적으로 관리하며 타 언어 배열의 기능을 동일하게 활용할 수 있으면서도 다양한 데이터타입을 포함할 수 있으며, 여러 내장 함수를 지원합니다.
- 단점 
    - 동적으로 크기를 관리하는 만큼 고정 배열에 비해 메모리를 효율적으로 관리하기 어렵고, 데이터의 일관성을 보장하기 어렵습니다. -> 고정이 필요하다면 튜플을 사용
    - 임의접근이 아닌 중간에 삽입/삭제 하는 경우는 크기가 커지면 커질수록 연산 성능이 떨어집니다. -> 리스트(배열)가 아닌 다른 집합 자료형을 사용해야 하지 않을까 생각합니다.


2. 일반적인 배열과  파이썬 리스트의 차이점은 무엇인가요? 
  - 배열은 요소의 타입이 고정됩니다.
  - 반면 리스트는 다양한 타입의 요소들을 포함할 수 있어요.


3. 정렬된 두 개의 리스트를 하나의 정렬된 리스트로 만드는 방법이 있을까요? 있다면 로직을 설명하시고 시간복잡도 측면에서도 설명해주세요.
  - 두 리스트를 append나 +로 연결하고, sort 함수로 정렬하면 O(nlogn) 의 시간복잡도로 가능해요.
  - 이미 정렬되어 있다면, 새로운 리스트 result=[]를 정의하고, a리스트와 b리스트의 첫 요소끼리 크기를 비교해서 작은 수부터 result 리스트에 삽입, 삽입된 값은 원래 리스트에서 제거하는 방법도 가능해요. 각 리스트의 요소가 n개라는 가정 하에 이 경우는 최악의 경우 2n회 연산이 발생하므로 시간복잡도는 O(n) 으료 표현할 수 있어요.


4. 정렬된 리스트와 정렬되지 않은 리스트에서 특정 원소를 탐색하는 방법에 대해 설명하고, 각 경우의 시간 복잡도에 대해 논해주세요.
  - 정렬되지 않은 리스트는 처음부터 순차적으로 선형 탐색합니다. 최악의 경우 모든 요소를 탐색하면서 O(n)의 시간복잡도를 가집니다.
  - 정렬된 리스트라면 up/down게임 하듯이 범위로 나누어서 찾는 방법이 효율적일 것 같아요. 이 경우는 절반씩 나누다보면 O(logn)의 시간복잡도를 가져요.


5. 파이썬에서 문자열을 순회하면서, 'abcde'에서 'bcdea', 'cdeab'처럼 앞뒤가 연결된 형태로 출력하려고 합니다. 리스트의 인덱스를 넘어설 때마다 이러한 순회를 효율적으로 구현하려면, 인덱스 계산을 어떻게 해야 할까요?

  - 모듈러 연산을 활용할 수 있습니다
```
string = "abcde"
for i in range(100):
    length = len(string)
    result = string[i%length:] + string[:i%length]
    print(result)
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

## 답:
```
def target_sum(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            pair = tuple(sorted([nums[i],nums[j]]))
            pairs.add(pair)
    # print(pairs)

    result = []
    for pair in pairs:
        if sum(pair) == target:
            result.append(pair)
    
    print(result)

    
target_sum([2,7,11,15], 9)
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
## 답
```
def findMaxConsecutive(nums):
    max_count = 0
    count = 0
    for i in nums:
        if i == 1:
            count +=1
            max_count = max(max_count, count)
        else:
            count = 0
    
    print(max_count)
    
nums = [1, 1, 0, 1, 1, 1]
findMaxConsecutive(nums)
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


## 답
```
def findDuplicates(nums):
    duplicates_nums = []
    for i in nums:
        if nums.count(i) > 1:
            duplicates_nums.append(i)
    duplicates_nums = list(set(duplicates_nums))
    print(duplicates_nums)

findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
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

## 답
```
def find_rotate_count(nums):
    sorted_nums = sorted(nums)

    for i in range(len(nums)):
        if nums == sorted_nums:
            print(i) #print count
        nums.append(nums[0])
        nums = nums[1:]

nums = [4, 5, 6, 7, 0, 1, 2]
find_rotate_count(nums)
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

## 답
```
def print_spiral(matrix):
    result = []
    row = len(matrix)
    col = len(matrix[0])
    
    top = 0
    bottom = row-1
    left = 0
    right = col-1
    
    while top<bottom and left<right:
        # 맨 윗 행 처리
        if top == 0:
            result.extend(matrix[top])
        else:
            result.extend(matrix[top][left:right+1])
        top+=1
        
        # 맨 끝 열 처리
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right -=1
        
        # 맨 아래 행 처리
        reversed_bottom = matrix[bottom][left:right+1]
        reversed_bottom.reverse()
        result.extend(reversed_bottom)
        bottom -=1
        
        # 맨 첫 열 처리
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        if bottom == top:
            result.append(matrix[top][bottom])
        left +=1
        
    print(result)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_spiral(matrix)
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

## 답
```
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

## 답
```
def consecutive_sum_max(nums, k):
    max_sum = 0
    for i in range(len(nums)-k):
        target_list = nums[i:i+k]
        target_sum = sum(target_list)
        if target_sum > max_sum:
            max_sum = target_sum
    print(max_sum)
    
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
consecutive_sum_max(nums, k)
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

## 답
```
def print_around(matrix,x,y):
    result = []
    for i in range(x-1,x+1+1):
        for j in range(y-1,y+1+1):
            if i == x and j == y:
                continue
            if i < 0 or j < 0:
                result.append("벗어났다")
                continue
            try:
                result.append(matrix[i][j])
            except IndexError:
                result.append("벗어났다")
    print(result)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
x = 1
y = 1

print_around(matrix,x,y)
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
## 답
```
비어있는 2차원 배열을 추가로 선언하고
  모든 좌표의 기본값은 0, 좌표 위치 자체가 지뢰인 경우는 'M'으로 표기
    좌표의 8방향 중 지뢰가 1개 있을 때 마다 해당 좌표의 값은-> +=1
  인덱스가 범위를 벗어난 경우 예외처리하고 카운트하지 않음
```

---

