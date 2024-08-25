04- 코딩준비 필수문법
2. 질문에 대한 답변

1. 리스트의 기본개념

리스트의 개념에 대해 정리해 주세요:

collection data type으로서 mutable object. 다음처럼 정의되고 index를 이용해 해당 값에 바로 접근가능하고 update도 가능함.

list1 = [1,2,3,4]

2. 리스트의 효율성

리스트의 임의접근의 시간 복잡도는?

list1 = [1,2,3,4] 인 경우 list1[2] 는 index 2인 값 3을 바로 접근가능하므로 O(1) 

리스트이 맨앞이나 중간에 데이터를 삽입할때 시간복잡도는?

list1.insert(0, 0) 처럼 0 index에 0을 삽입하는 경우 삽입이후 뒤에 오는 값들을 한개씩 다 이동해야 하므로 O(n)

list1.insert(2, 5) 처럼 2 index에 5을 삽입하는 경우도 삽입이후 뒤에 오는 값들을 전부 이동해야 하므로 O(n)

3. 튜플

-튜플의 개념과 리스트의 차이점: 

리스트는 mutable object, 튜플은 immutable object. 튜플은 리스트처럼 index 를 이용한 직접 접근이 가능하나 변경이 불가능.

- 튜플을 사용하는 것이 적법한 경우는 실행중 값의 변경을 원하지 않는 경우

4. Set()

셋의 개념과 특징:

중복된 값을 허용하지 않고 데이타 시퀀스가 중요하지 않다. 따라서 아무리 셋은 같은 값을 입력하더라도 오직 1개의 같은 값만 존재.

따라서 리스트의 정반대의 성격을 가지고 있다고 생각하면 됨. 셋은 인덱스를 통한 접근법은 존재하지 않고 같은 값이 여러개 존재할수 있음

﻿

5. 딕셔너리

딕셔너리 개념: key-value 로 이뤄진 자료구조로 key is unique. dict['a'] 처럼 key를 통해 값을 바로 얻을 수 있어 O(1) 의 시간복잡도를 가진다.

dict = {'a': [1,2,3], 'b':[4,5,6], 'c':[7,8,9]}

딕셔너리 키로 사용될 수 있는 데이타타입과 그 이유: immutable object인 int, string, tuple만 가능하며 키는 변경되지 않고 키에 mapping되는 value는 mutable object를 사용해서 Hash table을 관리한다.

딕셔너리에서 KVP를 insert, delete하는 time complexity는 key가 유니크한 값을 가지므로 O(1)

6. 성능비교문제

-리스트에서 pop(0) 와 collections.deque.popleft()의 동작방식이과 성능차이 이유:

리스트의 pop(0)는 index 0에 위치한 값을 끄집에 내고 리턴하며 나머지 값들을 앞으로 한칸씩 이동을 하게 되어 O(n)의 시간복잡도 발생

popleft()는 deque 맨앞에 있는 값을 제거하고 리턴하고 나머지 값들의 이동이 없어서 O(1)의 시간 복잡도 발생

stack.pop()은 스택의 맨뒤에 있는 값을 제거하고 리턴하는 것이라 역시 O(1)의 시간 복잡도발생

-리스트와 셋의 데이터 insert, remove time complexity:

list1.append() : add val to the last of the list: O(1)

list1.insert(0,3): add 3 to indext 0 position of the list: O(n)

pop(): remove and return the last value: O(1)

pop(i): remove val in index i: O(n) due to move all the values by one sequence after i position 

set data are consist of Hash table. 

set1.add(): O(1)

set1.remove(): O(1)

set1.pop(): O(1)

-주어진 데이터에서 고유한 값을 찾기 위해 리스트와 셋중 어떤 것을 사용하는 것이 유리:

리스트는 값의 중복을 허용하므로 앞에서부터 맨뒤까지 전부 탐색을 해야 하는 O(n)의 시간복잡도를 가지나 셋은 중복을 허용하지 않는 구조라 O(1)의 시간복잡도를 가지므로 셋이 휠씬 유리한 자료구조를 가지고 있음

7. 리스트 슬리이싱: 인덱스를 이용해서 리스트의 sub range를 얻는 방법

리스트 슬라이싱을 사용해 리스트의 부분배열을 얻는 방법:

list1 = [1,2,3,4,5]
list1[0:3] : [1,2,3] => index 0-2
list1[-1]: [5] => last index
list1[::-1] => reverse the list


코딩문제
문제 1: 리스트의 중복 제거 및 정렬

def remove_duplicates_and_sort(lst):
    seen = set()
    for i in range(len(lst)):
        seen.add(lst[i])
    lst2 = []
    while seen:
        lst2.append(seen.pop())
    
    sorted(lst2)
    
    return lst2

문제 2: 딕셔너리 키의 빈도수 계산

def count_word_frequencies(words):
    word_count = dict()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    return word_count

문제 3: 딕셔너리 키 존재 여부 확인

def key_exists(d, key):
    if key in d:
        return True
    return False


문제 4: 튜플의 요소 합

def sum_of_tuple(tpl):
    total = 0
    for t in tpl:
        total += t
    return total


문제 5: 리스트 슬라이싱으로 부분 리스트 추출

def slice_list(lst, start, end):
    return lst[start:end]



﻿
