
# C++ 우선순위 큐 (Priority Queue) 강의 자료

## 1. 우선순위 큐의 개념

### 1.1 기본 개념
우선순위 큐는 큐의 한 종류로, 각 요소에 우선순위가 부여되어 있으며, 높은 우선순위를 가진 요소가 먼저 처리되는 특성을 갖습니다. 일반적인 큐(FIFO: First-In-First-Out)와는 달리, 우선순위 큐는 요소가 삽입된 순서가 아닌 우선순위에 따라 제거됩니다. 이는 주로 힙(Heap) 자료구조를 이용해 구현됩니다.

### 1.2 일반 큐와 차이점
- **일반 큐**: FIFO(First-In-First-Out) 방식으로 작동하며, 먼저 들어온 요소가 먼저 나가는 구조입니다.
- **우선순위 큐**: 요소의 우선순위에 따라 정렬되어 있으며, 우선순위가 높은 요소가 먼저 나가는 구조입니다. 즉, 먼저 들어온 요소라도 우선순위가 낮으면 나중에 처리됩니다.

### 1.3 우선순위 큐의 유리한 점
우선순위 큐는 요소가 삽입될 때마다 자동으로 정렬되며, 이 과정에서 최대 힙 또는 최소 힙의 성질을 이용하여 O(log N)의 시간복잡도로 요소를 정렬합니다. 따라서 삽입, 삭제 연산이 매우 효율적이며, 정렬된 상태를 유지할 수 있습니다.

### 1.4 우선순위 큐를 사용해야 하는 상황
- **실시간 시스템**: 예를 들어, 운영체제의 작업 스케줄러는 우선순위 큐를 사용하여 우선순위가 높은 프로세스를 먼저 실행합니다.
- **네트워크 라우터**: 데이터 패킷의 전송 우선순위를 결정할 때 사용됩니다.
- **시뮬레이션 시스템**: 이벤트가 시간에 따라 처리될 때 우선순위 큐를 사용하여 가장 중요한 이벤트를 먼저 처리합니다.

## 2. 각 메서드의 동작 / 반환값 / 시간복잡도

| 메서드          | 동작                                       | 반환값               | 시간복잡도  |
|-----------------|------------------------------------------|--------------------|-----------|
| `push(value)`   | 큐에 요소를 삽입하고 정렬된 상태 유지       | 없음                | O(log N)  |
| `pop()`         | 가장 높은 우선순위의 요소를 제거            | 없음                | O(log N)  |
| `top()`         | 가장 높은 우선순위의 요소를 반환            | 가장 높은 우선순위 요소 | O(1)      |
| `empty()`       | 큐가 비어 있는지 확인                      | 비어 있으면 true     | O(1)      |
| `size()`        | 큐에 있는 요소의 개수를 반환                | 요소의 개수         | O(1)      |

## 3. 우선순위 큐에 사용자 정의 우선순위 함수를 정의하는 방법

C++에서 우선순위 큐의 기본 정렬은 내림차순(최대 힙)입니다. 사용자 정의 우선순위를 적용하려면 비교 함수(comparator)를 정의해야 합니다.

### 예시: 사용자 정의 비교 함수

```cpp
#include <iostream>
#include <queue>
#include <vector>

struct CustomCompare {
    bool operator()(int lhs, int rhs) {
        return lhs > rhs; // 오름차순으로 정렬
    }
};

int main() {
    std::priority_queue<int, std::vector<int>, CustomCompare> pq;
    pq.push(10);
    pq.push(5);
    pq.push(20);

    while (!pq.empty()) {
        std::cout << pq.top() << " ";
        pq.pop();
    }
    return 0;
}

// 출력 결과: 5 10 20
```

### 출력 결과 설명
- 위의 예시에서는 `CustomCompare`를 사용하여 우선순위 큐가 오름차순으로 작동하도록 설정했습니다.
- 우선순위 큐에 요소를 삽입한 후, 가장 낮은 값부터 출력됩니다. `20`이 가장 나중에 출력되는 이유는 `20`이 가장 큰 값이기 때문에 우선순위가 가장 낮아 맨 마지막에 처리되기 때문입니다.

## 4. 메서드 동작을 충분히 활용할 수 있는 예시 코드

### 예제: 고객 서비스 시스템에서의 우선순위 큐 사용

```cpp
#include <iostream>
#include <queue>
#include <string>
#include <vector>

struct Customer {
    std::string name;
    int priority;

    Customer(std::string n, int p) : name(n), priority(p) {}
};

struct CompareCustomer {
    bool operator()(Customer const& c1, Customer const& c2) {
        return c1.priority < c2.priority; // 우선순위가 높은 순으로 정렬
    }
};

int main() {
    std::priority_queue<Customer, std::vector<Customer>, CompareCustomer> customerQueue;

    customerQueue.push(Customer("Alice", 2));
    customerQueue.push(Customer("Bob", 5));
    customerQueue.push(Customer("Charlie", 1));

    while (!customerQueue.empty()) {
        Customer c = customerQueue.top();
        std::cout << "Serving customer: " << c.name << " with priority: " << c.priority << std::endl;
        customerQueue.pop();
    }

    return 0;
}

/*
출력 결과:
Serving customer: Bob with priority: 5
Serving customer: Alice with priority: 2
Serving customer: Charlie with priority: 1
*/
```
### 출력 결과 설명
- `CompareCustomer`를 통해 우선순위가 높은 고객이 먼저 처리되도록 설정하였습니다.
- `Bob`은 가장 높은 우선순위 `5`를 가지므로 가장 먼저 서비스됩니다.
- 다음으로 `Alice`가 우선순위 `2`를 가지며 처리되고, `Charlie`는 우선순위 `1`로 가장 나중에 처리됩니다.
- 우선순위 큐는 항상 우선순위가 높은 순으로 요소를 처리하기 때문에, 고객 서비스와 같은 시나리오에서 매우 유용하게 사용할 수 있습니다.
