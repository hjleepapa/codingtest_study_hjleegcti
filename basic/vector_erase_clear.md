
# C++의 `erase()`와 `clear()`의 차이점

제공된 C++ 코드에서는 벡터의 모든 요소를 제거하는 두 가지 방법인 `erase()`와 `clear()`의 실행 시간을 측정합니다. 일반적으로 결과는 `clear()`가 `erase()`보다 더 빠르다는 것을 보여줍니다. 
## 코드

```cpp
#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

int main() {
    // 5000만 개의 요소를 가진 벡터 생성
    size_t num_elements = 50000000;  // 벡터의 요소 개수 지정
    vector<int> vec(num_elements, 1);  // 5000만 개의 요소가 1로 초기화된 벡터 생성

    // erase() 함수의 실행 시간을 측정
    auto start_erase = chrono::high_resolution_clock::now();  // 현재 시간을 기록하여 시작 시간 저장
    vec.erase(vec.begin(), vec.end());  // 벡터의 모든 요소를 삭제 (시작부터 끝까지 삭제)
    auto end_erase = chrono::high_resolution_clock::now();  // 모든 요소 삭제 후 현재 시간 기록
    auto duration_erase = chrono::duration_cast<chrono::nanoseconds>(end_erase - start_erase);  // 시작과 끝 시간의 차이를 나노초로 계산
    cout << "erase() duration: " << duration_erase.count() << " nanoseconds" << endl;  // erase() 함수의 실행 시간 출력

    // 벡터를 다시 초기화
    vec = vector<int>(num_elements, 1);  // 벡터를 다시 5000만 개의 요소로 초기화

    // clear() 함수의 실행 시간을 측정
    auto start_clear = chrono::high_resolution_clock::now();  // clear() 함수 실행 전 현재 시간을 기록하여 시작 시간 저장
    vec.clear();  // 벡터의 모든 요소를 삭제
    auto end_clear = chrono::high_resolution_clock::now();  // 모든 요소 삭제 후 현재 시간 기록
    auto duration_clear = chrono::duration_cast<chrono::nanoseconds>(end_clear - start_clear);  // 시작과 끝 시간의 차이를 나노초로 계산
    cout << "clear() duration: " << duration_clear.count() << " nanoseconds" << endl;  // clear() 함수의 실행 시간 출력

    return 0;  // 프로그램 종료
}

// 예시 출력 (실제 시간은 시스템 및 환경에 따라 다를 수 있음)
// erase() duration: 150000000 nanoseconds
// clear() duration: 50000000 nanoseconds
```

## 왜 `clear()`가 `erase()`보다 빠른가?

### 1. **`erase()`의 내부 동작**:
   - `vec.erase(vec.begin(), vec.end())`를 사용할 때, 벡터는 지정된 범위 내의 요소를 개별적으로 제거합니다. 
   
### 2. **`clear()`의 내부 동작**:
   - 반면에 `clear()`는 벡터의 모든 요소를 한 번에 제거합니다. 이 함수는 벡터의 사이즈를 0으로 설정하고, 실제로는 기존의 메모리를 유지하며 요소들을 논리적으로만 제거합니다. 따라서 복사나 이동 작업이 필요 없으며, 매우 빠르게 완료됩니다.

### 3. **시간 복잡도**:
   - `erase()`의 시간 복잡도는 O(n)으로, n은 삭제하려는 요소의 수입니다. 
   - `clear()`의 시간 복잡도는 O(1)에 가깝습니다. 단순히 벡터의 크기를 0으로 설정하는 작업만 수행하기 때문입니다.
