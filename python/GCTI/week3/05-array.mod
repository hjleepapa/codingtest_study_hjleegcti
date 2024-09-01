기본 배열 질문
1. 파이썬에서 리스트의 장점 및 단점에 대해 말해주세요. 단점이 있다면 이를 해결할 수 있는 방법은 무엇이 있을까요?
리스트이 장점은 list1[3] = 7 처럼 인덱스를 통해 해당 값에 직접적으로 바로 접근할 수 있는 반면에 처음이나 중간에 값을 삭제하는 경우는 그 뒤의 값들을 한칸씩 다 옮겨야 해서 O(1)이 아닌 O(n)의 시간복잡도를 가지게 되는 문제발생

2. 일반적인 배열과 파이썬 리스트의 차이점은 무엇인가요?
일반적인 배열은 배열의 크기를 정해서 선언해야 하는데 파이썬의 경우는 특별히 크기를 미리 정할 필요없이 다이나믹하게 크기가 늘어나는 장점이 있음.

3. 정렬된 두 개의 리스트를 하나의 정렬된 리스트로 만드는 방법이 있을까요? 있다면 로직을 설명하시고 시간복잡도 측면에서도 설명해주세요.

list1 = [1,3,4,8,9]
list2 = [2,5,7,10]
# 두개의 정렬된 리스트를 while loop를 이용해 두개의 값들을 서로 비교하면서 두개중 작은 값들을 res 에 넣어주면서 다음값으로 이동하고 
# 결국에는 두개의 리스트중 큰값을 가진 리스트만 남겨지게 되서 그 리스트의 값을 res에 추가해 주면 됨
# Time Complexity: 두개의 리스트를 한번씩 쭉 검색비교해 나가므로 O(n)

i, j, m, n = 0, 0, len(list1), len(list2)
res = []
while i < m and j < n:
    if list1[i] < list2[j]:
        res.append(list1[i])
        i += 1
    else:
        res.append(list2[j])
        j += 1
if list1:
    res + list1[i:]
else:
    res + list2[j:]
print(res)



4. 정렬된 리스트와 정렬되지 않은 리스트에서 특정 원소를 탐색하는 방법에 대해 설명하고, 각 경우의 시간 복잡도에 대해 논해주세요.
N개의 정렬된 리스트에서 특정원소를 탐색하는 방법은 binary search를 통상사용해서 중간값을 기준으로 그보다 작은 지역을 탐색하느냐 큰 지역을 탐새하느냐 하면서 반으로 검색지역을 좁혀나가므로 O(logN)의 시간 복잡도를 가지게 됨.만약 정렬되지 않으면 일단 이것을 정렬하는데 O(NlogN)의 시간복잡도를 가지게 되어 그부분에서 차이가 발생.

5. 파이썬에서 문자열을 순회하면서, 'abcde'에서 'bcdea', 'cdeab'처럼 앞뒤가 연결된 형태로 출력하려고 합니다. 리스트의 인덱스를 넘어설 때마다 이러한 순회를 효율적으로 구현하려면, 인덱스 계산을 어떻게 해야 할까요?
아래에서 보여지는 코드처럼 문자열의 길이를 [0 - len(str1) - 1] 로 하는 리스트로 생각하고 MOD로 인덱스의 순회를 잘라주면 출력을 원하는 길이와 starting index가 주어지므로 간단히 구현이 가능

str1 = "abcde"
#       01234
expected_output = "cdeabcd" # len(7): 2(starting index) + 7(len) = 9
#                  2     

res = []
n = len(str1)
m = len(expected_output)

for i, c in enumerate(str1):
    if expected_output[0] == c:
        st_idx = i
        
for i in range(st_idx, st_idx + m):
    res.append(str1[i % n])

print("".join(res))

리스트의 합 문제
문제 설명: 주어진 정수 리스트에서 두 수의 합이 특정 목표 값이 되는 모든 쌍을 찾아라.
입력: 정수 리스트와 목표 정수
출력: 목표 값이 되는 모든 수 쌍 (중복 없이)
예시 (Python)
nums = [2, 7, 11, 15] target = 9 # 출력: [(2, 7)]

<Brute Force> Time Complexity: O(N^2)
nums = [2, 3, 4, 5, 7, 1, 8, 11, 15]
target = 9
# 출력: [(4, 5), (1,8), (2, 7)]

n = len(nums)
two_sum = set()
for i in range(n):
    for j in range(i+1, n):
        if nums[j] == target - nums[i]:
            two_sum.add((nums[i],nums[j]))
print(list(two_sum))


<One Pass Hash Table>: Time Complexity: O(N)

nums = [2, 3, 4, 5, 7, 1, 8, 11, 15]
target = 9
# 출력: [(4, 5), (1,8), (2, 7)]

two_sum = set()
d = dict()

for i, num in enumerate(nums):
    if num in d:
        two_sum.add((d[num], nums[i]))
    else:
        d[target - num] = nums[i]
print(list(two_sum))


연속된 1의 최대 길이
문제 설명: 0과 1로 이루어진 리스트에서 가장 긴 연속된 1의 길이를 찾아라.
입력: 0과 1로만 이루어진 리스트
출력: 가장 긴 연속된 1의 길이
예시 (Python)
nums = [1, 1, 0, 1, 1, 1] # 출력: 3
Time Complexity: O(N)

max_con_one = 0
res = 0

for i, num in enumerate(nums):
    if num == 1:
        max_con_one += 1
        res = max(max_con_one, res)
    else:
        max_con_one = 0

print(res)


중복 요소 찾기
문제 설명: 정수 리스트에서 중복된 숫자를 모두 찾아라.
입력: 정수 리스트
출력: 중복된 숫자의 리스트
예시 (Python)
nums = [4, 3, 2, 7, 8, 2, 3, 1] # 출력: [2, 3]
Time Complexity: O(N)

nums = [4, 3, 2, 7, 8, 2, 3, 1]
d = dict()
res = []

for num in nums:
    if num in d:
        res.append(num)
    else:
        d[num] = 1

print(res)


회전된 리스트의 회전 횟수 찾기
문제 설명: 주어진 리스트가 몇 번 회전되어 오름차순으로 정렬될 수 있는지 찾는 문제입니다. 원래 리스트는 오름차순으로 정렬된 상태에서 오른쪽으로 회전된 상태입니다.
입력: 정렬된 리스트가 오른쪽으로 회전된 상태의 리스트
출력: 리스트가 오름차순으로 정렬되기 위해 필요한 회전 횟수
예시 (Python)
nums = [4, 5, 6, 7, 0, 1, 2] # 출력: 4
Time Complexity: O(N)

num_of_rotate = 0

for i in range(len(nums)):
    if nums[0] < nums[-1]:
        break
    elif nums[i] <= nums[i+1] and i+1 < len(nums) - 1:
        num_of_rotate += 1
    else:
        num_of_rotate += 1
        break

print(num_of_rotate)


2D 리스트의 나선형 출력
문제 설명: N x N 크기의 2D 리스트를 나선형(spiral) 순서로 출력하라.
입력: N x N 2D 리스트
출력: 나선형 순서로 배열된 요소들의 리스트
예시 (Python)
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] # 출력: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 출력: [1, 2, 3, 6, 9, 8, 7, 4, 5]

m = len(matrix)
n = len(matrix[0])

L, T, R, B = 0, 0, n-1, m-1
res = []

while len(res) < m * n:
    for c in range(L, R+1):
        res.append(matrix[T][c])
    T += 1
    
    for r in range(T, B+1):
        res.append(matrix[r][R])
    R -= 1
    
    for c in range(R, L-1, -1):
        res.append(matrix[B][c])
    B -= 1
    
    for r in range(B, T-1, -1):
        res.append(matrix[r][L])
    L += 1
print(res)

리스트에서 모듈러 연산 문제
문제 설명: 주어진 리스트에서 각 요소를 k로 나눈 나머지를 계산하여 나머지가 같은 요소들이 몇 개 있는지 세어라.
입력: 정수 리스트와 나눌 수 k
출력: 나머지가 같은 요소들의 개수
예시 (Python)
nums = [2, 3, 5, 8, 10, 14] k = 3 # 출력: [(2, 4), (0, 1), (1, 1)] # 나머지가 2인 요소는 1개, 나머지가 0인 요소는 2개, 나머지가 1인 요소는 3개

nums = [2, 3, 5, 8, 10, 14]
k = 3
# 출력: [(2, 4), (0, 1), (1, 1)]  
# 나머지가 2인 요소는 1개, 나머지가 0인 요소는 2개, 나머지가 1인 요소는 3개
d = dict()
res = []

for num in nums:
    if num % k in d:
        d[num % k] += 1 
    
    else:
        d[num % k] = 1

for k, v in d.items():
    res.append((k,v))

print(res)


슬라이딩 윈도우 최대합 문제
문제 설명: 길이가 N인 정수 리스트에서 연속된 K개의 요소로 이루어진 부분 리스트의 최대 합을 찾아라.
입력: 정수 리스트와 정수 K
출력: 연속된 K개의 요소의 최대 합
예시 (Python)
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20] k = 4 # 출력: 39 # 부분 리스트 [4, 2, 10, 23]의 합이 39로 최대

nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
# 출력: 39  # 부분 리스트 [4, 2, 10, 23]의 합이 39로 최대

n = len(nums)
res = max_k_sum = float("-inf")


for i in range(n - k+ 1):
    max_k_sum = sum(nums[i:k+i])
    res = max(max_k_sum, res)    

print(res)


특정 좌표의 8방향 값 출력 문제
문제 설명: 주어진 2D 리스트에서 특정 좌표 (x, y)의 주변 8방향 값을 출력하라. 만약 범위를 벗어나는 경우, "벗어났다"라는 메시지를 출력해야 한다.
입력: N x M 2D 리스트, 좌표 (x, y)
출력: 특정 좌표의 8방향 값 또는 범위를 벗어난 경우 "벗어났다" 메시지 출력
예시 (Python)
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] x = 1 y = 1 # 출력: 1, 2, 3, 4, 6, 7, 8, 9 (모두 범위 내에 있음)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
x = 0 # column
y = 2 # row
# 출력: 1, 2, 3, 4, 6, 7, 8, 9  (모두 범위 내에 있음)

m = len(matrix)
n = len(matrix[0])
res = []

r, c = y, x
for nr, nc in [(r, c-1),(r-1, c-1),(r-1,c),(r-1, c+1),(r, c+1),(r+1, c-1),(r+1,c),(r+1,c+1)]:
    if 0 <= nr < m and 0 <= nc <= n:
        res.append(matrix[nr][nc])

if len(res) == 8:    
    print(sorted(res) , "(모두 범위 내에 있음)")
else:
    print(sorted(res), "(이외에는 범위를 벗어났다)")
    
지뢰 찾기 의사코드 작성 문제
문제 설명: 지뢰 찾기 게임에서 지뢰의 위치가 주어졌을 때, 각 빈 칸이 주변에 몇 개의 지뢰가 있는지 계산하는 로직을 의사코드로 작성하라.
입력: N x M 크기의 2D 리스트, 지뢰의 위치가 표시된 리스트
출력: 각 빈 칸의 지뢰 개수를 계산한 결과 리스트
예시 (Pseudo-Code)
Input: matrix = [ ['M', '.', '.', 'M'], ['.', '.', '.', '.'], ['.', 'M', '.', '.'] ]

Output: [ ['M', 1, 1, 'M'], [2, 2, 2, 1], [1, 'M', 1, 0] ]

<Pseudo-Code>
for r (length matrix row)
    for c (length matrix col)
        if matrix[r][c] is M
            move to next val
        if matrix[r][c] is '.'
            set count to 0
            for newR, newC (8 directions)
                if newR, newC are inside boundary and matrix[newR][newC] is 'M'
                    increment count
            update count to matrix[r][c]

위의 의사코드를 실제로 구현해 보면 아래와 같다.

matrix = [
  ['M', '.', '.', 'M'],
  ['.', '.', '.', '.'],
  ['.', 'M', '.', '.']
]

m = len(matrix)
n = len(matrix[0])

for r in range(m):
    for c in range(n):
        if matrix[r][c] == 'M':
            continue
        elif matrix[r][c] == '.':
            count = 0
        
            for nr, nc in [(r, c-1),(r-1, c-1),(r-1,c),(r-1, c+1),(r, c+1),(r+1, c-1),(r+1,c),(r+1,c+1)]:
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == 'M':
                    count += 1
            matrix[r][c] = count

print(matrix)
