
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
