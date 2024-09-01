
# C 언어 기초 문제

## 문제 1: 숫자 뒤집기
사용자로부터 정수를 입력받아 그 숫자를 거꾸로 출력하는 프로그램을 작성하세요.
- **예시 입력**: `12345`
- **예시 출력**: `54321`

## 문제 2: 구구단 출력
사용자로부터 1에서 9 사이의 숫자를 입력받아 해당 숫자의 구구단을 출력하는 프로그램을 작성하세요.
- **예시 입력**: `7`
- **예시 출력**: 
  ```
  7 * 1 = 7
  7 * 2 = 14
  7 * 3 = 21
  ...
  7 * 9 = 63
  ```

## 문제 3: 배열 내 최대값 찾기
사용자로부터 N개의 정수를 입력받아, 그 중에서 최대값을 찾는 프로그램을 작성하세요.
- **예시 입력**: `5`, `10 20 30 40 50`
- **예시 출력**: `50`

## 문제 4: 팩토리얼 계산
사용자로부터 정수를 입력받아 그 수의 팩토리얼을 계산하는 프로그램을 작성하세요.
- **예시 입력**: `5`
- **예시 출력**: `120` (5! = 5 * 4 * 3 * 2 * 1)

## 문제 5: 문자열에서 모음 개수 세기
사용자로부터 문자열을 입력받아, 그 문자열 내에 있는 모음(a, e, i, o, u)의 개수를 세는 프로그램을 작성하세요.
- **예시 입력**: `hello world`
- **예시 출력**: `3`

## 문제 6: 소수 판별 프로그램
사용자로부터 정수를 입력받아 그 수가 소수인지 아닌지 판별하는 프로그램을 작성하세요.
- **소수**: 1과 자기 자신으로만 나누어지는 1보다 큰 자연수.
- **예시 입력**: `7`
- **예시 출력**: `7은 소수입니다.`

## 문제 7: 피보나치 수열 출력
사용자로부터 정수 N을 입력받아, N번째 피보나치 수를 출력하는 프로그램을 작성하세요.
- **피보나치 수열**: 첫 두 항이 0과 1이며, 이후의 모든 항은 바로 앞 두 항의 합인 수열.
- **예시 입력**: `10`
- **예시 출력**: `34`

## 문제 8: 2차원 배열의 행과 열의 합
사용자로부터 2차원 배열의 크기(NxM)와 각 요소를 입력받아, 각 행과 열의 합을 계산하는 프로그램을 작성하세요.
- **예시 입력**:
  ```
  3 3
  1 2 3
  4 5 6
  7 8 9
  ```
- **예시 출력**:
  ```
  행의 합: 6 15 24
  열의 합: 12 15 18
  ```

## 문제 9: 문자열 압축
사용자로부터 문자열을 입력받아 연속되는 문자를 압축하여 표현하는 프로그램을 작성하세요.
- **예시 입력**: `aaabbbcccaaa`
- **예시 출력**: `a3b3c3a3`

## 문제 10: 배열의 원소 정렬
사용자로부터 N개의 정수를 입력받아, 이를 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요.
- **예시 입력**: `5 3 8 1 2`
- **예시 출력**: `1 2 3 5 8`


<details>
<summary>해설</summary>


# C 언어 기초 문제 해설

## 문제 1: 숫자 뒤집기

### 해설
이 문제는 입력받은 정수를 문자열로 변환한 후, 그 문자열을 뒤집어서 다시 정수로 변환하는 과정을 통해 해결할 수 있습니다.

### 답안 코드
```c
#include <stdio.h>

int main() {
    int num, reversed = 0;
    printf("정수를 입력하세요: ");
    scanf("%d", &num);

    while (num != 0) {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }

    printf("뒤집은 숫자: %d\n", reversed);
    return 0;
}
```

## 문제 2: 구구단 출력

### 해설
입력받은 숫자의 구구단을 출력하기 위해, 1부터 9까지의 숫자를 곱해 그 결과를 출력하는 간단한 반복문을 사용합니다.

### 답안 코드
```c
#include <stdio.h>

int main() {
    int num;
    printf("출력할 구구단의 숫자를 입력하세요 (1-9): ");
    scanf("%d", &num);

    for (int i = 1; i <= 9; i++) {
        printf("%d * %d = %d\n", num, i, num * i);
    }
    return 0;
}
```

## 문제 3: 배열 내 최대값 찾기

### 해설
사용자로부터 입력받은 여러 정수 중에서 최대값을 찾기 위해, 배열을 사용하여 모든 값을 저장한 뒤 반복문을 통해 최대값을 찾습니다.

### 답안 코드
```c
#include <stdio.h>

int main() {
    int n;
    printf("정수의 개수를 입력하세요: ");
    scanf("%d", &n);

    int arr[n];
    printf("정수를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    printf("최대값: %d\n", max);
    return 0;
}
```

## 문제 4: 팩토리얼 계산

### 해설
팩토리얼 계산은 반복문을 사용하여 입력된 정수부터 1까지의 모든 수를 곱하는 방식으로 구현할 수 있습니다.

### 답안 코드
```c
#include <stdio.h>

int main() {
    int num;
    unsigned long long factorial = 1;
    printf("정수를 입력하세요: ");
    scanf("%d", &num);

    for (int i = 1; i <= num; i++) {
        factorial *= i;
    }

    printf("%d의 팩토리얼: %llu\n", num, factorial);
    return 0;
}
```

## 문제 5: 문자열에서 모음 개수 세기

### 해설
이 문제는 입력받은 문자열을 한 글자씩 검사하면서 모음인지 확인하고, 모음일 경우 그 개수를 증가시키는 방식으로 해결합니다.

### 답안 코드
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int vowels = 0;
    printf("문자열을 입력하세요: ");
    scanf("%[^
]%*c", str);  // 문자열 입력

    for (int i = 0; i < strlen(str); i++) {
        char ch = str[i];
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            vowels++;
        }
    }

    printf("모음의 개수: %d\n", vowels);
    return 0;
}
```

## 문제 6: 소수 판별 프로그램

### 해설
소수는 1과 자기 자신으로만 나누어 떨어지는 수입니다. 따라서, 2부터 그 수의 제곱근까지 나누어 떨어지는 수가 있는지 검사하여 소수 여부를 판별할 수 있습니다.

### 답안 코드
```c
#include <stdio.h>
#include <math.h>

int main() {
    int num, isPrime = 1;
    printf("정수를 입력하세요: ");
    scanf("%d", &num);

    if (num < 2) {
        isPrime = 0;
    } else {
        for (int i = 2; i <= sqrt(num); i++) {
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }
    }

    if (isPrime) {
        printf("%d은(는) 소수입니다.\n", num);
    } else {
        printf("%d은(는) 소수가 아닙니다.\n", num);
    }

    return 0;
}
```

## 문제 7: 피보나치 수열 출력

### 해설
피보나치 수열의 각 항은 바로 앞 두 항의 합으로 결정됩니다. 이를 반복문이나 재귀함수를 이용해 구현할 수 있습니다.

### 답안 코드
```c
#include <stdio.h>

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    printf("피보나치 수열의 N번째 항을 입력하세요: ");
    scanf("%d", &n);

    printf("%d번째 피보나치 수는 %d입니다.\n", n, fibonacci(n));
    return 0;
}
```

## 문제 8: 2차원 배열의 행과 열의 합

### 해설
이 문제는 2차원 배열의 각 행과 열의 합을 계산하기 위해 중첩 반복문을 사용하여 해결할 수 있습니다.

### 답안 코드
```c
#include <stdio.h>

int main() {
    int n, m;
    printf("2차원 배열의 크기(NxM)를 입력하세요: ");
    scanf("%d %d", &n, &m);

    int arr[n][m];
    printf("배열 요소를 입력하세요:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    printf("행의 합: ");
    for (int i = 0; i < n; i++) {
        int rowSum = 0;
        for (int j = 0; j < m; j++) {
            rowSum += arr[i][j];
        }
        printf("%d ", rowSum);
    }
    printf("\n");

    printf("열의 합: ");
    for (int j = 0; j < m; j++) {
        int colSum = 0;
        for (int i = 0; i < n; i++) {
            colSum += arr[i][j];
        }
        printf("%d ", colSum);
    }
    printf("\n");

    return 0;
}
```

## 문제 9: 문자열 압축

### 해설
문자열을 반복하면서 연속되는 문자의 개수를 세고, 이를 압축된 형태로 표현하여 출력하는 프로그램입니다.

### 답안 코드
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    printf("문자열을 입력하세요: ");
    scanf("%s", str);

    int n = strlen(str);
    for (int i = 0; i < n; i++) {
        int count = 1;
        while (i < n - 1 && str[i] == str[i + 1]) {
            count++;
            i++;
        }
        printf("%c%d", str[i], count);
    }
    printf("\n");

    return 0;
}
```

## 문제 10: 배열의 원소 정렬

### 해설
배열의 원소를 정렬하기 위해 다양한 알고리즘이 사용될 수 있습니다. 여기서는 가장 기본적인 버블 정렬을 사용하여 오름차순으로 정렬합니다.

### 답안 코드
```c
#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int n;
    printf("정수의 개수를 입력하세요: ");
    scanf("%d", &n);

    int arr[n];
    printf("정수를 입력하세요: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    bubbleSort(arr, n);

    printf("정렬된 배열: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```

  
</details>
