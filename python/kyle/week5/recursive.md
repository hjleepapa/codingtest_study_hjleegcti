### 문제 1: 숫자의 각 자리수를 거꾸로 나열하기

#### 문제 설명:
양의 정수 n이 주어졌을 때, n의 각 자리수를 재귀를 사용하여 거꾸로 나열한 값을 반환하는 함수를 작성하세요.

#### 예시 입/출력:
- 입력: `n = 12345`
- 출력: `54321`

#### 설명:
정수 12345를 재귀적으로 처리하여 54321이 반환됩니다.

#### 제한 사항:
- n은 1 이상 1,000,000 이하의 자연수입니다.

#### 답
```
def reverse_number(n):
    if n < 1:
        return ''
    mod = n%10
    n = n//10
    return str(mod) + reverse_number(n)
    
print(reverse_number(12345))
```


### 문제 2: 이진수를 십진수로 변환하기

#### 문제 설명:
이진수로 표현된 문자열이 주어졌을 때, 해당 이진수를 재귀를 사용하여 십진수로 변환하는 함수를 작성하세요.

#### 예시 입/출력:
- 입력: `binary_str = "1101"`
- 출력: `13`

#### 설명:
이진수 1101은 십진수로 변환하면 13이 됩니다.

#### 제한 사항:
- 문자열의 길이는 1 이상 32 이하입니다.
- 이진수는 `0`과 `1`로만 구성되어 있습니다.

#### 답
```
def bynary_to_decimal(binary_str):
    degree = len(binary_str)-1
    if degree == 0:
        return 1*int(binary_str[0])
    return 2**degree*int(binary_str[0]) + bynary_to_decimal(binary_str[1:])

print(bynary_to_decimal("1")) # 13
```

### 문제 3: 문자열 압축하기

#### 문제 설명:
문자열이 주어졌을 때, 재귀를 사용하여 동일한 문자가 연속될 경우 그 문자의 반복 횟수를 세어 압축한 문자열을 반환하는 함수를 작성하세요.

#### 예시 입/출력:
- 입력: `s = "aaabccccdd"`
- 출력: `"a3b1c4d2"`

#### 설명:
연속된 문자를 카운트하여 "a3b1c4d2"가 반환됩니다.

#### 제한 사항:
- 문자열의 길이는 1 이상 1,000 이하입니다.

#### 답
```
def compress_string(s):
    if not s:
        return ""
    count = 0
    for i in s:
        if i == s[0]:
            count +=1
        else:
            break
    return s[0] + str(count) + compress_string(s[count:])

print(compress_string("aaabccccdd")) # "a3b1c4d2"
```


### 문제 4: 하노이의 탑 문제

#### 문제 설명:
3개의 기둥과 N개의 원판이 주어졌을 때, 재귀를 사용하여 하노이의 탑 문제를 해결하는 알고리즘을 작성하세요. 모든 원판을 첫 번째 기둥에서 세 번째 기둥으로 옮기는 과정을 출력하세요.

#### 예시 입/출력:
- 입력: `N = 3`
- 출력:
  ```
  Move disk 1 from A to C
  Move disk 2 from A to B
  Move disk 1 from C to B
  Move disk 3 from A to C
  Move disk 1 from B to A
  Move disk 2 from B to C
  Move disk 1 from A to C
  ```

#### 제한 사항:
- 원판의 개수 N은 1 이상 20 이하입니다.


#### 답
```
def hanoi_recursieve(n):
    def move(n, start, end):
        print(f"Move disk {n} from {start} to {end}")

    def hanoi(n, start, end, temp):
        if n == 1:
            move(n, start, end)
        else:
            hanoi(n - 1, start, temp, end)
            move(n, start, end)
            hanoi(n - 1, temp, end, start)

    hanoi(n, 'A', 'C', 'B')
hanoi_recursieve(3)
```

### 문제 5: 숫자 분해하기

#### 문제 설명:
양의 정수 n이 주어졌을 때, n을 두 정수의 곱으로 분해하는 모든 방법을 찾는 재귀 함수를 작성하세요.

#### 예시 입/출력:
- 입력: `n = 12`
- 출력: `[(1, 12), (2, 6), (3, 4)]`

#### 설명:
12를 두 정수의 곱으로 나타내면 (1, 12), (2, 6), (3, 4)와 같이 분해됩니다.

#### 제한 사항:
- n은 1 이상 10,000 이하의 정수입니다.


#### 답
```
def disassemble(n):
    def devide(n, divisor):
        if divisor > n // divisor:
            return []
        if n % divisor == 0:
            return [(divisor, n // divisor)] + devide(n, divisor + 1)
        return devide(n, divisor + 1)    
    return devide(n, 1)

print(disassemble(12))
```
