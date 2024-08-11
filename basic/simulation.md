
# 시뮬레이션 연습

## 1. 배열의 90도 회전

### 기본 개념
배열의 90도 회전이란, 2차원 배열을 기준으로 모든 요소를 시계 방향으로 90도 회전시키는 작업입니다. 이 작업은 배열의 행(row)을 열(column)로 변환하고, 위치를 조정하는 과정을 포함합니다.

### 상세한 설명
만약 `n x n` 배열이 있다고 가정하면, 이 배열의 90도 회전은 다음과 같이 이루어집니다:
- 0번째 행의 마지막 요소는 0번째 열의 첫 번째 요소가 됩니다.
- 1번째 행의 마지막 요소는 1번째 열의 첫 번째 요소가 됩니다.
- 이러한 패턴이 배열의 모든 요소에 적용됩니다.

<details>
<summary>실전 문제</summary>


# 문제: 3x3 행렬 90도 회전

3x3 정수 행렬이 주어졌을 때, 이 행렬을 시계 방향으로 90도 회전시키는 프로그램을 작성하세요. 아래 주어진 코드를 완성하여 이 기능을 구현하세요.

## 주어진 코드

c
#include <stdio.h>

void rotate90(int arr[3][3]); // 배열을 90도로 회전하는 함수 (문제에선 3x3 한정)
void print(int* arr[3][3]); // 배열을 출력하는 함수 (문제에선 3x3 한정)

int matrix[3][3] = 
{
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};

int main()
{
    rotate90(matrix); // 행렬을 90도 회전시키는 함수 호출
    print(matrix);    // 회전된 행렬을 출력하는 함수 호출
    
    return 0;     
}


## 구현해야 할 함수

1. **rotate90 함수**
   - **기능**: 3x3 행렬을 시계 방향으로 90도 회전시킵니다.
   - **입력**: 3x3 행렬의 시작 주소를 가리키는 포인터.
   - **반환**: 없음. 입력된 행렬 자체를 수정하여 회전된 결과를 반영합니다.

2. **print 함수**
   - **기능**: 3x3 행렬을 출력합니다.
   - **입력**: 3x3 행렬의 시작 주소를 가리키는 포인터.
   - **반환**: 없음. 행렬의 각 요소를 출력합니다.

## 요구사항

1. rotate90 함수를 작성하여 3x3 행렬을 시계방향으로 90도 회전시키세요. 
    - 이 함수는 매개변수로 주어진 3x3 행렬을 수정하여, 원래의 행렬을 시계 방향으로 90도 회전한 결과로 만듭니다.
2. print 함수를 작성하여 3x3 행렬을 출력하세요.
    - 이 함수는 3x3 행렬을 매개변수로 받아 행과 열을 구분하여 출력해야 합니다.
  
</details>

<details>
<summary>해설</summary>

# 문제: 3x3 행렬 90도 회전 - 정답 및 해설 (주석 추가 버전)

## 정답 코드

다음은 주석을 추가하여 이해하기 쉽게 만든 정답 코드입니다:

c
#include <stdio.h>

// 3x3 배열을 시계 방향으로 90도 회전시키는 함수
void rotate90(int arr[3][3]) {
    int temp; // 임시 변수로 값을 저장
    // 행렬의 4개 모서리 요소를 교환하여 회전시키는 과정
    for (int i = 0; i < 2; i++) { // 첫 번째 루프: 행렬의 왼쪽 상단부터 시작
        for (int j = i; j < 2 - i; j++) { // 두 번째 루프: 행렬의 해당 열을 따라 이동
            // 사각형의 4개의 요소를 시계 방향으로 한 칸씩 이동
            temp = arr[i][j]; // 첫 번째 요소를 임시 변수에 저장
            arr[i][j] = arr[2-j][i]; // 네 번째 요소를 첫 번째 요소로 이동
            arr[2-j][i] = arr[2-i][2-j]; // 세 번째 요소를 네 번째 요소로 이동
            arr[2-i][2-j] = arr[j][2-i]; // 두 번째 요소를 세 번째 요소로 이동
            arr[j][2-i] = temp; // 임시 변수에 저장된 첫 번째 요소를 두 번째 요소로 이동
        }
    }
}

// 3x3 배열을 출력하는 함수
void print(int arr[3][3]) {
    // 행렬의 각 요소를 출력
    for(int i = 0; i < 3; i++) { // 첫 번째 루프: 행렬의 각 행을 따라 이동
        for(int j = 0; j < 3; j++) { // 두 번째 루프: 행렬의 각 열을 따라 이동
            printf("%d ", arr[i][j]); // 현재 요소를 출력
        }
        printf("\n"); // 행이 끝날 때 줄 바꿈
    }
}

int matrix[3][3] = 
{
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};

int main() {
    rotate90(matrix); // 행렬을 90도 회전시키는 함수 호출
    print(matrix);    // 회전된 행렬을 출력하는 함수 호출
    
    return 0;     
}

  
</details>

## 2. 달팽이 수열

### 기본 개념
달팽이 수열이란, 2차원 배열의 첫 번째 행부터 시작하여 배열의 경계를 따라 시계 방향으로 나선형으로 진행하면서 숫자를 채워 넣는 방식입니다. 이 방법은 배열의 모든 요소를 순서대로 채우기 위해 사용됩니다.

### 상세한 설명
달팽이 수열을 구현하려면 다음과 같은 단계를 따릅니다:
1. 왼쪽에서 오른쪽으로 이동하여 숫자를 채운 후,
2. 위에서 아래로 내려가면서 채우고,
3. 오른쪽에서 왼쪽으로 이동하며 채우고,
4. 아래에서 위로 올라가면서 채웁니다.
5. 이 과정을 배열이 채워질 때까지 반복합니다.



<details>
<summary>실전 문제</summary>

# 문제: 달팽이 수열 생성

정수 n이 주어질 때, 1부터 n^2까지의 수를 달팽이 모양으로 배치한 n x n 행렬을 생성하는 프로그램을 작성하세요. 아래 주어진 코드를 완성하여 이 기능을 구현하세요.

## 주어진 코드

```c
#include <stdio.h>

void generateSnailArray(int n, int arr[n][n]); // 달팽이 수열을 생성하는 함수
void printArray(int n, int arr[n][n]); // 배열을 출력하는 함수

int main()
{
    int n = 4; // 예시로 4x4 달팽이 수열을 생성
    int arr[n][n];
    
    generateSnailArray(n, arr); // 달팽이 수열을 생성하는 함수 호출
    printArray(n, arr);         // 생성된 수열을 출력하는 함수 호출
    
    return 0;     
}
```

## 구현해야 할 함수

1. **generateSnailArray 함수**
   - **기능**: 1부터 n^2까지의 수를 달팽이 모양으로 배치한 n x n 행렬을 생성합니다.
   - **입력**: n과 n x n 배열의 시작 주소를 가리키는 포인터.
   - **반환**: 없음. 입력된 배열 자체를 수정하여 달팽이 수열을 반영합니다.

2. **printArray 함수**
   - **기능**: n x n 행렬을 출력합니다.
   - **입력**: n과 n x n 배열의 시작 주소를 가리키는 포인터.
   - **반환**: 없음. 행렬의 각 요소를 출력합니다.

## 요구사항

1. `generateSnailArray` 함수를 작성하여 n x n 행렬을 달팽이 모양으로 채우세요. 
    - 이 함수는 매개변수로 주어진 n과 배열을 사용하여, 1부터 n^2까지의 수를 시계 방향으로 돌며 달팽이 형태로 채웁니다.
2. `printArray` 함수를 작성하여 n x n 행렬을 출력하세요.
    - 이 함수는 n x n 행렬을 매개변수로 받아 행과 열을 구분하여 출력해야 합니다.

</details>

<details>
<summary>해설</summary>

# 문제: 달팽이 수열 생성 - 정답 및 해설 (주석 추가 버전)

## 정답 코드

다음은 주석을 추가하여 이해하기 쉽게 만든 정답 코드입니다:

```c
#include <stdio.h>

// n x n 달팽이 수열을 생성하는 함수
void generateSnailArray(int n, int arr[n][n]) {
    int value = 1;
    int min_row = 0, max_row = n-1;
    int min_col = 0, max_col = n-1;
    
    while (value <= n * n) {
        for (int i = min_col; i <= max_col && value <= n * n; i++) {
            arr[min_row][i] = value++;
        }
        min_row++;
        
        for (int i = min_row; i <= max_row && value <= n * n; i++) {
            arr[i][max_col] = value++;
        }
        max_col--;
        
        for (int i = max_col; i >= min_col && value <= n * n; i--) {
            arr[max_row][i] = value++;
        }
        max_row--;
        
        for (int i = max_row; i >= min_row && value <= n * n; i--) {
            arr[i][min_col] = value++;
        }
        min_col++;
    }
}

// n x n 배열을 출력하는 함수
void printArray(int n, int arr[n][n]) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n = 4; // 예시로 4x4 달팽이 수열을 생성
    int arr[n][n];
    
    generateSnailArray(n, arr); // 달팽이 수열을 생성하는 함수 호출
    printArray(n, arr);         // 생성된 수열을 출력하는 함수 호출
    
    return 0;     
}
```

</details>

## 3. 배열을 2차원 좌표로 해서 상하좌우 이동

### 기본 개념
2차원 배열에서 상하좌우로 이동하는 것은, 특정 좌표에서 상, 하, 좌, 우의 인접한 요소로 이동하는 것을 의미합니다. 이 과정은 주로 탐색 알고리즘이나 게임에서 자주 사용됩니다.

### 상세한 설명
2차원 배열에서 현재 위치에서 상하좌우로 이동하려면, 각각의 방향에 대한 좌표 변화를 이해해야 합니다:
- 상: `row - 1, col`
- 하: `row + 1, col`
- 좌: `row, col - 1`
- 우: `row, col + 1`

이동할 때 배열의 경계를 넘어가는지 확인하는 것이 중요합니다.


<details>
<summary>실전 문제</summary>

# 문제: 2D 배열에서 상하좌우 이동

n x n 크기의 2D 정수 배열과 시작 좌표가 주어질 때, 상하좌우로 이동하여 특정 경로를 따라 이동하는 프로그램을 작성하세요. 

## 이동 경로 설명

이동 경로는 문자열로 주어지며, 각 문자는 이동 방향을 나타냅니다:

- `U`는 위쪽(Up)으로 한 칸 이동
- `D`는 아래쪽(Down)으로 한 칸 이동
- `L`는 왼쪽(Left)으로 한 칸 이동
- `R`는 오른쪽(Right)으로 한 칸 이동

예를 들어, 주어진 경로 문자열이 `UURDDL`이라면:
1. 시작 위치에서 위로 두 칸 이동 (`UU`)
2. 오른쪽으로 한 칸 이동 (`R`)
3. 아래로 두 칸 이동 (`DD`)
4. 마지막으로 왼쪽으로 한 칸 이동 (`L`)

## 주어진 코드

```c
#include <stdio.h>

void moveIn2DArray(int n, int arr[n][n], int start_x, int start_y, char* moves); // 상하좌우 이동을 수행하는 함수
void printArray(int n, int arr[n][n]); // 배열을 출력하는 함수

int main()
{
    int n = 5; // 예시로 5x5 배열을 생성
    int arr[5][5] = {0}; // 초기 배열은 0으로 채움
    int start_x = 2, start_y = 2; // 시작 좌표를 배열의 중앙으로 설정
    char moves[] = "UURDDL"; // 예시 이동 경로: 위, 위, 오른쪽, 아래, 아래, 왼쪽
    
    moveIn2DArray(n, arr, start_x, start_y, moves); // 이동을 수행하는 함수 호출
    printArray(n, arr); // 이동 후의 배열을 출력하는 함수 호출
    
    return 0;     
}
```

## 구현해야 할 함수

1. **moveIn2DArray 함수**
   - **기능**: 주어진 시작 좌표에서 상하좌우 이동을 수행하여 배열을 업데이트합니다.
   - **입력**: n과 n x n 배열, 시작 좌표 (start_x, start_y), 이동 경로를 나타내는 문자열 moves.
   - **반환**: 없음. 입력된 배열 자체를 수정하여 이동 경로를 반영합니다.

2. **printArray 함수**
   - **기능**: n x n 배열을 출력합니다.
   - **입력**: n과 n x n 배열.
   - **반환**: 없음. 배열의 각 요소를 출력합니다.

## 요구사항

1. `moveIn2DArray` 함수를 작성하여 상하좌우 이동을 수행하세요.
    - 이 함수는 주어진 시작 좌표에서 상(U), 하(D), 좌(L), 우(R)로 이동합니다. 이동한 위치에 1을 기록합니다.
    - 배열의 경계를 넘어가는 경우, 해당 이동은 무시합니다.
2. `printArray` 함수를 작성하여 n x n 배열을 출력하세요.
    - 이 함수는 n x n 배열을 매개변수로 받아 행과 열을 구분하여 출력해야 합니다.

</details>

<details>
<summary>해설</summary>

# 문제: 2D 배열에서 상하좌우 이동 - 정답 및 해설

## 정답 코드

다음은 주석을 추가하여 이해하기 쉽게 만든 정답 코드입니다:

```c
#include <stdio.h>

// 상하좌우 이동을 수행하는 함수
void moveIn2DArray(int n, int arr[n][n], int start_x, int start_y, char* moves) {
    int x = start_x;
    int y = start_y;
    
    arr[x][y] = 1; // 시작 위치에 1을 기록
    
    for (int i = 0; moves[i] != '\0'; i++) {
        if (moves[i] == 'U' && x > 0) x--; // 위로 이동
        else if (moves[i] == 'D' && x < n-1) x++; // 아래로 이동
        else if (moves[i] == 'L' && y > 0) y--; // 왼쪽으로 이동
        else if (moves[i] == 'R' && y < n-1) y++; // 오른쪽으로 이동
        
        arr[x][y] = 1; // 이동한 위치에 1을 기록
    }
}

// n x n 배열을 출력하는 함수
void printArray(int n, int arr[n][n]) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n = 5; // 예시로 5x5 배열을 생성
    int arr[5][5] = {0}; // 초기 배열은 0으로 채움
    int start_x = 2, start_y = 2; // 시작 좌표를 배열의 중앙으로 설정
    char moves[] = "UURDDL"; // 예시 이동 경로: 위, 위, 오른쪽, 아래, 아래, 왼쪽
    
    moveIn2DArray(n, arr, start_x, start_y, moves); // 이동을 수행하는 함수 호출
    printArray(n, arr); // 이동 후의 배열을 출력하는 함수 호출
    
    return 0;     
}
```

</details>

