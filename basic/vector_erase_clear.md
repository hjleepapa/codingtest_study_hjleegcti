
# C++의 `erase()`와 `clear()`의 차이점

제공된 C++ 코드에서는 벡터의 모든 요소를 제거하는 두 가지 방법인 `erase()`와 `clear()`의 실행 시간을 측정합니다. 일반적으로 결과는 `clear()`가 `erase()`보다 더 빠르다는 것을 보여줍니다. 이러한 현상이 발생하는 이유를 MIT 교수 수준으로 설명해보겠습니다.

## 코드

```cpp
#include <iostream>
#include <vector>
#include <chrono>

int main() {
    // 5000만 개의 요소를 가진 벡터 생성
    size_t num_elements = 50000000;
    std::vector<int> vec(num_elements, 1);

    // erase() 함수의 실행 시간을 측정
    auto start_erase = std::chrono::high_resolution_clock::now();
    vec.erase(vec.begin(), vec.end()); // 모든 요소 삭제
    auto end_erase = std::chrono::high_resolution_clock::now();
    auto duration_erase = std::chrono::duration_cast<std::chrono::nanoseconds>(end_erase - start_erase);
    std::cout << "erase() duration: " << duration_erase.count() << " nanoseconds" << std::endl;

    // 벡터를 다시 초기화
    vec = std::vector<int>(num_elements, 1);

    // clear() 함수의 실행 시간을 측정
    auto start_clear = std::chrono::high_resolution_clock::now();
    vec.clear();
    auto end_clear = std::chrono::high_resolution_clock::now();
    auto duration_clear = std::chrono::duration_cast<std::chrono::nanoseconds>(end_clear - start_clear);
    std::cout << "clear() duration: " << duration_clear.count() << " nanoseconds" << std::endl;

    return 0;
}
```

## 왜 `clear()`가 `erase()`보다 빠른가?

### 1. **`erase()`의 내부 동작**:
   - `vec.erase(vec.begin(), vec.end())`를 사용할 때, 벡터는 지정된 범위 내의 요소를 개별적으로 제거합니다. 이는 각 요소를 삭제하고 그 뒤의 모든 요소들을 앞으로 이동시키는 작업을 수행해야 함을 의미합니다. 이러한 작업은 많은 요소가 있을 경우 매우 비용이 많이 들며, 결과적으로 더 많은 시간이 소요됩니다.
   
### 2. **`clear()`의 내부 동작**:
   - 반면에 `clear()`는 벡터의 모든 요소를 한 번에 제거합니다. 이 함수는 벡터의 사이즈를 0으로 설정하고, 실제로는 기존의 메모리를 유지하며 요소들을 논리적으로만 제거합니다. 따라서 복사나 이동 작업이 필요 없으며, 매우 빠르게 완료됩니다.

### 3. **시간 복잡도**:
   - `erase()`의 시간 복잡도는 O(n)으로, n은 삭제하려는 요소의 수입니다. 각 요소가 삭제될 때마다 나머지 요소들이 앞으로 이동해야 하기 때문입니다. 
   - `clear()`의 시간 복잡도는 O(1)에 가깝습니다. 단순히 벡터의 크기를 0으로 설정하는 작업만 수행하기 때문입니다.

## 결론

`clear()`는 벡터의 모든 요소를 효율적으로 제거하며, 내부 메모리를 재할당하지 않고 크기만 0으로 설정하기 때문에 성능이 더 좋습니다. 반면, `erase()`는 각 요소를 개별적으로 삭제하고 나머지 요소를 이동시키는 작업을 수행해야 하므로 더 느립니다. 이러한 차이는 많은 수의 요소가 있는 경우에 더욱 두드러지게 나타납니다.
