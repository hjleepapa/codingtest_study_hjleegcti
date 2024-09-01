
# 배열 (Array)

## 배열의 기본 개념
배열은 동일한 데이터 타입의 요소를 연속적으로 저장하는 자료 구조입니다. 배열은 고정된 크기를 가지며, 인덱스를 사용하여 요소에 접근할 수 있습니다. 배열의 첫 번째 요소는 인덱스 0에서 시작합니다.

## 배열의 임의 접근
배열은 임의 접근(Random Access)이 가능하여, 인덱스를 통해 원하는 위치의 요소에 즉시 접근할 수 있습니다. 이 접근은 시간 복잡도가 O(1)로 매우 효율적입니다.



## 배열의 활용

배열은 여러 가지 방식으로 활용될 수 있습니다. 이 문서에서는 **대칭**, **대각선 이동**, **2차원 좌표 표현**에 대해 자세히 설명합니다.

### 1. 대칭 (Symmetry)

대칭이란 배열의 요소를 특정 축을 기준으로 반사시키는 작업입니다. 일반적으로 사용되는 대칭의 유형은 두 가지입니다:

- **수평 대칭 (Horizontal Symmetry)**: 배열의 가로축을 기준으로 상하 반전을 수행하는 대칭입니다.
- **수직 대칭 (Vertical Symmetry)**: 배열의 세로축을 기준으로 좌우 반전을 수행하는 대칭입니다.

#### 예시: 수평 및 수직 대칭

원본 배열:
|   |   |   |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

- **수평 대칭** 결과:
  
|   |   |   |
|---|---|---|
| 7 | 8 | 9 |
| 4 | 5 | 6 |
| 1 | 2 | 3 |

- **수직 대칭** 결과:

|   |   |   |
|---|---|---|
| 3 | 2 | 1 |
| 6 | 5 | 4 |
| 9 | 8 | 7 |

#### 수평 및 수직 대칭을 위한 코드 예제 (C++)

```cpp
#include <iostream>
#include <algorithm> // reverse 함수에 필요

using namespace std;

int main() {
    // 원래 배열 정의
    const int rows = 3; // 행의 수
    const int cols = 3; // 열의 수
    int original_array[rows][cols] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // 수평 대칭 배열 생성 (행 순서 뒤집기)
    // 핵심 공식: horizontal_symmetric[i][j] = original_array[rows - i - 1][j];
    int horizontal_symmetric[rows][cols];
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            horizontal_symmetric[i][j] = original_array[rows - i - 1][j];
        }
    }

    // 수평 대칭 결과 출력
    cout << "Horizontal Symmetric:" << endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << horizontal_symmetric[i][j] << " ";
        }
        cout << endl;
    }
    // 출력 결과:
    // Horizontal Symmetric:
    // 7 8 9
    // 4 5 6
    // 1 2 3

    // 수직 대칭 배열 생성 (각 행의 열 순서 뒤집기)
    // 핵심 공식: vertical_symmetric[i][j] = original_array[i][cols - j - 1];
    int vertical_symmetric[rows][cols];
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            vertical_symmetric[i][j] = original_array[i][cols - j - 1];
        }
    }

    // 수직 대칭 결과 출력
    cout << "Vertical Symmetric:" << endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << vertical_symmetric[i][j] << " ";
        }
        cout << endl;
    }
    // 출력 결과:
    // Vertical Symmetric:
    // 3 2 1
    // 6 5 4
    // 9 8 7

    return 0;
}
```

### 2. 대각선 이동 (Diagonal Movement)

대각선 이동은 2차원 배열의 요소를 대각선 방향으로 이동시키는 작업을 말합니다. 대각선 이동은 주로 두 가지 방향으로 수행될 수 있습니다:

- **왼쪽 위에서 오른쪽 아래로 이동** (↘)
- **왼쪽 아래에서 오른쪽 위로 이동** (↗)

#### 예시: 대각선 이동

원본 배열:
|   |   |   |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

- **왼쪽 위에서 오른쪽 아래로 이동 (↘)**:
  
이동 후 배열:
  
|   |   |   |
|---|---|---|
| 1 |   |   |
|   | 5 |   |
|   |   | 9 |

- **왼쪽 아래에서 오른쪽 위로 이동 (↗)**:

이동 후 배열:

|   |   |   |
|---|---|---|
|   |   | 3 |
|   | 5 |   |
| 7 |   |   |

#### 대각선 이동을 위한 코드 예제 (C++)

```cpp
#include <iostream>
#include <cstddef> // for NULL

using namespace std;

int main() {
    // 원래 배열 정의
    const int size = 3; // 3x3 배열
    int original_array[size][size] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // 왼쪽 위에서 오른쪽 아래로 대각선 이동 배열 생성
    // 핵심 공식: diagonal_down[i][j] = (i == j) ? original_array[i][j] : NULL;
    int diagonal_down[size][size];
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (i == j) {
                diagonal_down[i][j] = original_array[i][j];
            } else {
                diagonal_down[i][j] = NULL; // 대각선 이외의 값은 NULL
            }
        }
    }

    // 왼쪽 위에서 오른쪽 아래로 대각선 이동 결과 출력
    cout << "Diagonal Down:" << endl;
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (diagonal_down[i][j] != NULL) {
                cout << diagonal_down[i][j] << " ";
            } else {
                cout << "None ";
            }
        }
        cout << endl;
    }
    // 출력 결과:
    // Diagonal Down:
    // 1 None None
    // None 5 None
    // None None 9

    // 왼쪽 아래에서 오른쪽 위로 대각선 이동 배열 생성
    // 핵심 공식: diagonal_up[i][j] = (i + j == size - 1) ? original_array[i][j] : NULL;
    int diagonal_up[size][size];
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (i + j == size - 1) {
                diagonal_up[i][j] = original_array[i][j];
            } else {
                diagonal_up[i][j] = NULL; // 대각선 이외의 값은 NULL
            }
        }
    }

    // 왼쪽 아래에서 오른쪽 위로 대각선 이동 결과 출력
    cout << "Diagonal Up:" << endl;
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            if (diagonal_up[i][j] != NULL) {
                cout << diagonal_up[i][j] << " ";
            } else {
                cout << "None ";
            }
        }
        cout << endl;
    }
    // 출력 결과:
    // Diagonal Up:
    // None None 3
    // None 5 None
    // 7 None None

    return 0;
}
```

### 3. 2차원 좌표 표현

2차원 배열은 좌표 공간을 표현하는 데 자주 사용됩니다. 각 배열의 요소는 특정 위치를 나타내는 좌표로 간주할 수 있습니다. 예를 들어, 3x3 배열에서 각 요소의 인덱스 `(i, j)`는 해당 요소의 위치를 나타냅니다.

#### 예시: 2차원 좌표 표현

원본 배열:
|   |   |   |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

이 배열에서 `5`의 위치는 `(1, 1)`이며, `9`의 위치는 `(2, 2)`입니다.

#### 좌표 공간 내에서의 이동

좌표 공간 내에서 요소를 이동시키는 작업은 특정 요소를 새로운 좌표로 옮기는 것으로 이해할 수 있습니다. 예를 들어, `5`를 `(2, 0)`으로 이동시키면 배열은 다음과 같이 됩니다:

|   |   |   |
|---|---|---|
| 1 | 2 | 3 |
| 4 |   | 6 |
| 5 | 8 | 9 |

이와 같은 방법으로 2차원 배열을 사용하여 좌표 공간에서의 다양한 이동과 대칭 작업을 표현할 수 있습니다.

#### 오픗뎃 배열 활용 (C++)
```cpp

#include <iostream>
#include <vector>
using namespace std;

// 2차원 좌표에서 주변 8개 방향을 탐색하기 위한 dx, dy 배열
// dx와 dy는 각각 x축과 y축의 이동을 나타냅니다.
// 예를 들어, dx[0], dy[0]은 좌상(-1, -1)을 의미합니다.
int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0}; // 행 방향으로의 이동: 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1}; // 열 방향으로의 이동: 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌

int main() {
    // 3x3 2차원 배열 생성 및 초기화
    vector<vector<int>> arr = {
        {1, 2, 3}, // 첫 번째 행
        {4, 5, 6}, // 두 번째 행
        {7, 8, 9}  // 세 번째 행
    };

    // 탐색을 시작할 좌표 (1, 1) 설정
    // 이 좌표는 배열의 중앙에 위치하고 있으며, 값은 5입니다.
    int x = 1, y = 1; // 중앙 위치 (1, 1)
    cout << "현재 위치: (" << x << ", " << y << "), 값: " << arr[x][y] << endl;

    // 주변 8개 방향을 순회하며 값 출력
    // for 루프는 각 방향을 탐색하기 위해 8번 반복됩니다.
    // 핵심 공식: nx = x + dx[i], ny = y + dy[i]
    // 이 공식은 현재 위치 (x, y)에서 dx[i], dy[i]만큼 이동하여 새로운 좌표 (nx, ny)를 계산합니다.
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i]; // 새로운 x 좌표 (현재 x에 dx[i]를 더한 값)
        int ny = y + dy[i]; // 새로운 y 좌표 (현재 y에 dy[i]를 더한 값)

        // 배열의 범위를 벗어나지 않는지 확인
        // nx와 ny가 배열의 유효한 인덱스인지 검사합니다.
        if (nx >= 0 && nx < arr.size() && ny >= 0 && ny < arr[0].size()) {
            // 범위를 벗어나지 않으면 해당 위치의 값 출력
            // 유효한 인덱스라면, 해당 위치의 값을 출력합니다.
            cout << "이웃 위치: (" << nx << ", " << ny << "), 값: " << arr[nx][ny] << endl;
        }
    }

    // 예상 출력:
    // 현재 위치: (1, 1), 값: 5
    // 이웃 위치: (0, 0), 값: 1
    // 이웃 위치: (0, 1), 값: 2
    // 이웃 위치: (0, 2), 값: 3
    // 이웃 위치: (1, 2), 값: 6
    // 이웃 위치: (2, 2), 값: 9
    // 이웃 위치: (2, 1), 값: 8
    // 이웃 위치: (2, 0), 값: 7
    // 이웃 위치: (1, 0), 값: 4

    return 0;
}

```

## 배열을 vector로 많이 표현하는 이유
C++에서 배열을 대신하여 vector를 많이 사용하는 이유는 유연성과 편의성 때문입니다. vector는 크기를 동적으로 변경할 수 있고, 메모리 관리가 자동으로 이루어지기 때문에 배열보다 더 안전하고 효율적으로 사용할 수 있습니다.

## 배열을 사용할 때 효율적인 경우
- 고정된 크기의 데이터를 다룰 때
- 메모리 사용량이 중요할 때
- 임의 접근이 빈번하게 발생할 때

## 배열을 사용할 때 비효율적인 경우
- 데이터 크기가 동적으로 변하는 경우
- 배열의 크기를 자주 변경해야 하는 경우
- 삽입/삭제 작업이 빈번할 때

# 벡터 (Vector)

## vector의 기본 개념
vector는 동적 배열(dynamic array)로, C++의 표준 라이브러리에서 제공하는 템플릿 클래스입니다. vector는 크기를 동적으로 조정할 수 있으며, 자동으로 메모리를 관리합니다.

## vector의 특성
- 동적 크기 조정
- 임의 접근 가능
- 자동 메모리 관리
- 다양한 메서드를 통한 편리한 데이터 조작

## vector의 초기화

### 1차원 벡터 초기화
```cpp
vector<int> vec1; // 빈 벡터 생성
vector<int> vec2(10); // 10개의 요소를 가지는 벡터 생성, 초기값은 0
vector<int> vec3(10, 5); // 10개의 요소를 가지는 벡터 생성, 초기값은 5
```

### 2차원 벡터 초기화
```cpp
vector<vector<int>> vec2D(10, vector<int>(10)); // 10x10 2차원 벡터 생성, 모든 요소 초기값은 0
```

## vector의 메서드

| 메서드명    | 시간복잡도 | 반환값   | 동작                                    |
|-------------|------------|----------|-----------------------------------------|
| `push_back` | O(1)*      | 없음     | 벡터의 끝에 요소를 추가                 |
| `pop_back`  | O(1)       | 없음     | 벡터의 마지막 요소를 제거               |
| `size`      | O(1)       | 크기     | 벡터의 현재 크기를 반환                 |
| `clear`     | O(n)       | 없음     | 모든 요소를 제거                        |
| `empty`     | O(1)       | bool     | 벡터가 비어있는지 여부를 반환           |
| `at`        | O(1)       | 요소값   | 지정한 인덱스의 요소에 접근             |

### 메서드 동작을 익힐 수 있는 코드 예시
```cpp

#include <iostream>
#include <vector>
using namespace std;

// 2차원 좌표에서 주변 8개 방향을 탐색하기 위한 dx, dy 배열
// dx와 dy는 각각 x축과 y축의 이동을 나타냅니다.
// 예를 들어, dx[0], dy[0]은 좌상(-1, -1)을 의미합니다.
int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0}; // 행 방향으로의 이동: 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1}; // 열 방향으로의 이동: 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌

int main() {
    // 3x3 2차원 배열 생성 및 초기화
    vector<vector<int>> arr = {
        {1, 2, 3}, // 첫 번째 행
        {4, 5, 6}, // 두 번째 행
        {7, 8, 9}  // 세 번째 행
    };

    // 탐색을 시작할 좌표 (1, 1) 설정
    // 이 좌표는 배열의 중앙에 위치하고 있으며, 값은 5입니다.
    int x = 1, y = 1; // 중앙 위치 (1, 1)
    cout << "현재 위치: (" << x << ", " << y << "), 값: " << arr[x][y] << endl;

    // 주변 8개 방향을 순회하며 값 출력
    // for 루프는 각 방향을 탐색하기 위해 8번 반복됩니다.
    // 핵심 공식: nx = x + dx[i], ny = y + dy[i]
    // 이 공식은 현재 위치 (x, y)에서 dx[i], dy[i]만큼 이동하여 새로운 좌표 (nx, ny)를 계산합니다.
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i]; // 새로운 x 좌표 (현재 x에 dx[i]를 더한 값)
        int ny = y + dy[i]; // 새로운 y 좌표 (현재 y에 dy[i]를 더한 값)

        // 배열의 범위를 벗어나지 않는지 확인
        // nx와 ny가 배열의 유효한 인덱스인지 검사합니다.
        if (nx >= 0 && nx < arr.size() && ny >= 0 && ny < arr[0].size()) {
            // 범위를 벗어나지 않으면 해당 위치의 값 출력
            // 유효한 인덱스라면, 해당 위치의 값을 출력합니다.
            cout << "이웃 위치: (" << nx << ", " << ny << "), 값: " << arr[nx][ny] << endl;
        }
    }

    // 예상 출력:
    // 현재 위치: (1, 1), 값: 5
    // 이웃 위치: (0, 0), 값: 1
    // 이웃 위치: (0, 1), 값: 2
    // 이웃 위치: (0, 2), 값: 3
    // 이웃 위치: (1, 2), 값: 6
    // 이웃 위치: (2, 2), 값: 9
    // 이웃 위치: (2, 1), 값: 8
    // 이웃 위치: (2, 0), 값: 7
    // 이웃 위치: (1, 0), 값: 4

    return 0;
}

```
