from collections import Counter

# 3. 정렬된 두 개의 리스트를 하나의 정렬된 리스트로 만드는 방법이 있을까요? 있다면 로직을 설명하시고 시간복잡도 측면에서도 설명해주세요.
def solution(arr1, arr2):
    arr1 = arr1 + arr2
    arr1.sort()

    return arr1

print(solution([1, 3, 4], [1, 2, 3]))    # [1, 1, 2, 3, 3, 4]
print(solution([5, 6], [1, 2, 3, 4]))    # [1, 2, 3, 4, 5, 6]

# 5. 파이썬에서 문자열을 순회하면서, 'abcde'에서 'bcdea', 'cdeab'처럼 앞뒤가 연결된 형태로 출력하려고 합니다. 리스트의 인덱스를 넘어설 때마다 이러한 순회를 효율적으로 구현하려면, 인덱스 계산을 어떻게 해야 할까요?
def solution(s):
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        print(rotated)

print(solution('abcde'))

# 리스트의 합 문제
def solution(nums, target):
    answer = []
    
    n = len(nums)
    nums.sort()
    start = 0
    end = n - 1

    while start < end:
        sum = nums[start] + nums[end]

        if sum == target:
            answer.append((nums[start], nums[end]))
            start += 1
            end -= 1
        elif sum > target:
            end -= 1
        else:
            start += 1

    return answer

print(solution([2, 7, 11, 15], 9))

# 연속된 1의 최대 길이
def solution(nums):
    count = 0
    max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
        
    return max(count, max_count)

print(solution([1, 1, 0, 1, 1, 1]))
print(solution([1, 1, 1, 1, 1, 1]))
print(solution([1, 1, 1, 1, 0, 0]))

# 중복 요소 찾기
def solution(nums):
    answer = []

    num_dict = dict(Counter(nums))
    
    for k, v in num_dict.items():
        if v > 1:
            answer.append(k)
    
    return answer

print(solution([4, 3, 2, 7, 8, 2, 3, 1]))

# 회전된 리스트의 회전 횟수 찾기
def solution(nums):
    sorted_nums = list(sorted(nums))
    idx = nums.index(sorted_nums[0])

    return idx

print(solution([4, 5, 6, 7, 0, 1, 2]))

# 2D 리스트의 나선형 출력
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


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 리스트에서 모듈러 연산 문제
def solution(nums, k):
    num_dict = {}

    for num in nums:
        target = num % k

        if target in num_dict:
            num_dict[target] += 1
        else:
            num_dict[target] = 1
    
    return list(num_dict.items())

print(solution([2, 3, 5, 8, 10, 14], 3))

# 슬라이딩 윈도우 최대합 문제
def solution(nums, k):
    sub_sum = 0
    max_sum = 0

    for i in range(len(nums)):
        sub_list = nums[i:i + k]
        
        if len(sub_list) == k:
            sub_sum = sum(sub_list)
            max_sum = max(sub_sum, max_sum)
    
    return max_sum
    
print(solution([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))

# 특정 좌표의 8방향 값 출력 문제
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

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))    # 1, 2, 3, 4, 6, 7, 8, 9
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 0))    # 벗어났다

# 지뢰 찾기 의사코드 작성 문제
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

print(solution([['M', '.', '.', 'M'], ['.', '.', '.', '.'], ['.', 'M', '.', '.']]))    # [['M', 1, 1, 'M'], [2, 2, 2, 1], [1, 'M', 1, 0]]