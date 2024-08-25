# 1. 리스트의 기본 개념
- 시퀀스(순서)가 있는 자료형
- 인덱싱 및 슬라이싱 가능
  - 인덱싱이란 인덱스를 활용해서 특정 위치의 원소에 접근하는 것
  - 슬라이싱이란 범위를 지정해서 값들을 복사하여 가져오는 것

# 2. 리스트의 효율성
- 다양한 데이터 타입 포함 가능
- 동적으로 크기 조절
- 특정 인덱스에 접근하는 연산의 시간 복잡도 O(1)
- 리스트 끝에 요소를 추가하거나 제거하는 연산의 시간 복잡도 O(1)
  - 단, 리스트 중간에 요소를 추가하거나 제거하는 연산의 시간 복잡도 O(N)
    - 리스트의 나머지 요소를 이동시켜야 하기 때문

# 3. 튜플
- 한 번 생성하면 삽입 및 삭제 불가
- 인덱싱 및 슬라이싱은 가능

# 4. 셋 (Set)
- 고유한 값을 저장하는 데이터 구조
  - 수학에서의 집합과 유사
- 중복 불허
- 순서가 없기 때문에 인덱스를 이용해 요소에 접근 불가

# 5. 딕셔너리
- 키와 쌍을 저장하는 해시 테이블
- 키를 사용하여 값을 검색하는 자료형

# 6. 성능 비교 문제
|데이터 타입|인덱스 접근|삽입|삭제|
|--------|--------|---|---|
|리스트|O(1)|O(1)|O(N)|
|튜플|O(1)|-|-|
|셋|-|O(1)|O(1)|
|딕셔너리|O(1)|O(1)|O(N)|

# 7. 리스트 슬라이싱
- 범위를 지정해서 값들을 복사해서 가져오는 방식
- list_name[a:b] 형태로 작성하는데, 이 코드는 인덱스 a 이상부터 b 미만에 해당하는 원소를 새 리스트에 담아 반환
```python
my_list = [1, 2, 3, 4, 5]
my_list[0:2]    # [1, 2]
my_list[1:]     # [2, 3, 4, 5]
my_list[3:4]    # [4]
my_list[-4:-2]  # [2, 3]
```

---

# 코딩 문제

## 문제 1: 리스트의 중복 제거 및 정렬
리스트 `lst`가 주어졌을 때, 리스트 내 중복된 요소를 제거하고 남은 요소들을 오름차순으로 정렬한 새로운 리스트를 반환하는 함수를 작성하세요.
```python
def remove_duplicates_and_sort(lst):
    return sorted(set(list))

# 예시
print(remove_duplicates_and_sort([4, 2, 2, 1, 3, 4]))  # 출력: [1, 2, 3, 4]
print(remove_duplicates_and_sort([5, 5, 5, 5]))  # 출력: [5]
print(remove_duplicates_and_sort([1, 2, 3, 4, 5]))  # 출력: [1, 2, 3, 4, 5]
```

## 문제 2: 딕셔너리 키의 빈도수 계산
문자열 리스트 `words`가 주어졌을 때, 각 단어가 리스트에 등장하는 빈도수를 딕셔너리로 반환하는 함수를 작성하세요.
```python
def count_word_frequencies(words):
    my_dict = {}
    
    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    
    return my_dict

# 예시
print(count_word_frequencies(["apple", "banana", "apple", "orange", "banana", "apple"]))  
# 출력: {'apple': 3, 'banana': 2, 'orange': 1}
print(count_word_frequencies(["dog", "cat", "dog", "dog", "fish"]))  
# 출력: {'dog': 3, 'cat': 1, 'fish': 1}
```

## 문제 3: 딕셔너리 키 존재 여부 확인
딕셔너리 d와 키 key가 주어졌을 때, 해당 키가 딕셔너리에 존재하는지 여부를 반환하는 함수를 작성하세요.
```python
def key_exists(d, key):
    return key in d

# 예시
print(key_exists({"name": "Alice", "age": 25}, "name"))  # 출력: True
print(key_exists({"name": "Alice", "age": 25}, "address"))  # 출력: False
print(key_exists({}, "key"))  # 출력: False
```

## 문제 4: 튜플의 요소 합
튜플 tpl이 주어졌을 때, 튜플 내 모든 요소의 합을 반환하는 함수를 작성하세요.
```python
def sum_of_tuple(tpl):
    sum = 0

    for t in tpl:
        sum += t
    
    return sum

# 예시
print(sum_of_tuple((1, 2, 3, 4)))  # 출력: 10
print(sum_of_tuple((5,)))  # 출력: 5
print(sum_of_tuple(()))  # 출력: 0
```

## 문제 5: 리스트 슬라이싱으로 부분 리스트 추출
리스트 lst와 두 개의 정수 start, end가 주어졌을 때, 주어진 범위에 해당하는 부분 리스트를 반환하는 함수를 작성하세요. start 인덱스는 포함되며, end 인덱스는 포함되지 않습니다.
```python
def slice_list(lst, start, end):
    # 구현하세요

# 예시
print(slice_list([10, 20, 30, 40, 50], 1, 3))  # 출력: [20, 30]
print(slice_list([1, 2, 3, 4, 5], 0, 5))  # 출력: [1, 2, 3, 4, 5]
print(slice_list([7, 8, 9], 1, 1))  # 출력: []
```