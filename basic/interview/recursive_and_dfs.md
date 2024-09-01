
# 목차
1. [재귀 함수에서 '재귀 깊이'를 줄이기 위한 방법](#재귀-함수에서-재귀-깊이를-줄이기-위한-방법)
2. [함수 호출 스택에서의 메모리 누수 문제와 방지 방법](#함수-호출-스택에서의-메모리-누수-문제와-방지-방법)
3. [스택 기반 메모리 관리와 힙 기반 메모리 관리 비교](#스택-기반-메모리-관리와-힙-기반-메모리-관리-비교)
4. [순환 그래프에서 모든 사이클을 탐지하는 DFS 알고리즘](#순환-그래프에서-모든-사이클을-탐지하는-dfs-알고리즘)
5. [재귀적 백트래킹에서의 'Combinatorial Explosion' 문제 해결 전략](#재귀적-백트래킹에서의-combinatorial-explosion-문제-해결-전략)
6. [DFS를 사용하는 것이 BFS보다 유리한 경우](#dfs를-사용하는-것이-bfs보다-유리한-경우)
7. [실전 문제](#실전-문제)
    - [문제 1: 피보나치 수열 계산](#문제-1-피보나치-수열-계산)
    - [문제 2: 이진 트리의 최대 깊이 찾기](#문제-2-이진-트리의-최대-깊이-찾기)
    - [문제 3: 방향성 그래프에서 경로 탐색](#문제-3-방향성-그래프에서-경로-탐색)

---

## 재귀 깊이를 줄이기 위한 방법

### 1. 메모이제이션 (Memoization)

메모이제이션은 이미 계산한 결과를 저장하여 중복 계산을 피하는 방법입니다. 이를 통해 불필요한 재귀 호출을 줄일 수 있습니다.

```java
import java.util.HashMap;
import java.util.Map;

public class FibonacciMemoization {
    private static Map<Integer, Integer> memo = new HashMap<>();

    public static int fibonacci(int n) {
        // 이미 계산된 값이 있는 경우, 그 값을 반환
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        // 기본 케이스
        if (n <= 1) {
            return n;
        }
        // 결과를 메모에 저장
        int result = fibonacci(n - 1) + fibonacci(n - 2);
        memo.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(10));  // Output: 55
    }
}
```

### 2. 반복적 접근 (Iterative Approach)

재귀 대신 반복문을 사용하여 같은 기능을 수행하는 방식입니다. 반복문을 사용하면 재귀 호출 스택을 사용하지 않으므로 재귀 깊이 문제를 피할 수 있습니다.

```java
public class FibonacciIterative {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        int a = 0, b = 1, c = 0;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(10));  // Output: 55
    }
}
```


## 함수 호출 스택에서의 메모리 누수 문제와 방지 방법

메모리 누수는 함수 호출 스택에서 메모리가 해제되지 않고 남아있어 발생하는 문제입니다. 특히 재귀 함수에서 적절한 종료 조건이 없거나 잘못 설정된 경우 이러한 문제가 발생할 수 있습니다. 방지 방법은 다음과 같습니다:

- **종료 조건 설정:** 재귀 함수의 기저 사례를 명확히 정의하여 모든 재귀 호출이 종료되도록 합니다.
- **자원 관리:** 파일, 소켓 등 외부 자원을 사용하는 경우, 사용 후 반드시 자원을 해제하도록 합니다.
- **정적 분석 도구 사용:** 메모리 누수 문제를 감지할 수 있는 정적 분석 도구를 사용하여 코드 품질을 점검합니다.

## 예시 코드

### 메모리 누수가 발생하는 예시 코드

다음은 자바에서 메모리 누수가 발생할 수 있는 예시 코드입니다. 이 코드에서는 재귀 함수 호출에서 잘못된 종료 조건이 설정되어 있어 무한 재귀 호출이 발생하며 메모리 누수가 생길 수 있습니다.

```java
public class MemoryLeakExample {
    public static void recursiveFunction(int num) {
        // 잘못된 종료 조건: num이 항상 감소하지 않는다면 무한 재귀 호출 발생 가능
        if (num > 0) {
            System.out.println("Number: " + num);
            recursiveFunction(num); // num이 변하지 않음, 무한 재귀 호출
        }
    }

    public static void main(String[] args) {
        recursiveFunction(5); // 프로그램이 종료되지 않고 메모리 누수 발생 가능
    }
}
```

### 메모리 누수를 방지하는 코드

다음은 올바른 종료 조건을 설정하여 메모리 누수를 방지하는 예시 코드입니다. 이 코드는 재귀 호출 시 매번 `num` 값을 감소시키며, 결국 종료 조건을 만족하여 재귀 호출이 종료됩니다.

```java
public class MemoryLeakPrevention {
    public static void recursiveFunction(int num) {
        // 올바른 종료 조건: num이 0 이하일 때 재귀 호출 종료
        if (num > 0) {
            System.out.println("Number: " + num);
            recursiveFunction(num - 1); // num이 감소하여 종료 조건으로 수렴
        }
    }

    public static void main(String[] args) {
        recursiveFunction(5); // 재귀 호출이 종료되고 메모리 누수 방지
    }
}
```

### 예시 2: 객체 참조를 해제하지 않는 경우

아래 코드는 객체를 배열에 저장한 후, 사용하지 않는 객체를 참조에서 제거하지 않아 메모리 누수가 발생할 수 있는 예시입니다.

```java
import java.util.ArrayList;
import java.util.List;

public class ObjectMemoryLeakExample {
    public static void main(String[] args) {
        List<int[]> list = new ArrayList<>();
        while (true) {
            int[] largeArray = new int[1000000]; // 큰 배열 생성
            list.add(largeArray); // 배열을 리스트에 추가
            // 사용하지 않는 객체를 참조에서 제거하지 않아 메모리 누수 발생 가능
        }
    }
}
```

### 메모리 누수를 방지하는 코드

다음 코드는 사용 후 필요 없는 객체 참조를 명시적으로 제거하여 메모리 누수를 방지하는 예시입니다.

```java
import java.util.ArrayList;
import java.util.List;

public class ObjectMemoryLeakPrevention {
    public static void main(String[] args) {
        List<int[]> list = new ArrayList<>();
        while (true) {
            int[] largeArray = new int[1000000]; // 큰 배열 생성
            list.add(largeArray); // 배열을 리스트에 추가
            if (list.size() > 100) {
                list.clear(); // 필요 없는 객체 참조를 제거하여 메모리 누수 방지
            }
        }
    }
}
```

위 예시를 통해 외부 자원을 사용할 때와 객체 참조를 관리할 때 메모리 누수를 방지하는 방법을 배울 수 있습니다.



## 스택 기반 메모리 관리와 힙 기반 메모리 관리 비교

- **스택 기반 메모리 관리:**  
  함수 호출 시 자동으로 메모리가 할당되고, 함수가 종료되면 자동으로 해제됩니다. 빠르고 효율적이지만, 할당 가능한 메모리 크기가 제한적입니다. 일반적으로 지역 변수나 함수의 매개변수를 저장하는 데 사용됩니다. 스택 메모리는 LIFO(Last In, First Out) 방식으로 작동하며, 스택 오버플로우(overflow)의 위험이 있습니다.

- **힙 기반 메모리 관리:**  
  프로그램 실행 중 동적으로 메모리를 할당하고 필요 시 해제합니다. 메모리 크기에 제한이 적으나, 할당과 해제에 시간이 더 걸리고 메모리 누수 가능성이 있습니다. 힙 메모리는 크기가 비교적 크며, 동적 데이터 구조(예: 연결 리스트, 트리, 그래프)를 저장하는 데 주로 사용됩니다. 올바르게 메모리를 해제하지 않으면 메모리 누수가 발생할 수 있습니다.

### 예시 코드: 스택 기반 메모리 관리 (Java)

```java
public class StackExample {
    public static void function() {
        int stackVar = 10;  // 스택에 할당된 변수
        System.out.println("스택 변수의 값: " + stackVar);
    }  // function이 종료되면 stackVar 메모리는 자동으로 해제됨

    public static void main(String[] args) {
        function();  // 함수 호출
    }
}
```

위 코드에서 `stackVar`는 함수 `function()` 내부에서 선언된 지역 변수로, 스택 메모리에 할당됩니다. 함수가 호출되면 `stackVar`가 스택에 할당되고, 함수가 종료되면 자동으로 스택에서 해제됩니다. 이는 메모리 관리가 자동으로 이루어지며 매우 빠르게 작동합니다.

### 예시 코드: 힙 기반 메모리 관리
```java
public class HeapExample {
    public static void function() {
        Integer heapVar = new Integer(20);  // 힙에 메모리 할당
        System.out.println("힙 변수의 값: " + heapVar);
        // heapVar는 가비지 컬렉터에 의해 자동으로 해제됨
    }

    public static void main(String[] args) {
        function();  // 함수 호출
    }
}
```

이 예제에서는 `heapVar`가 `new` 연산자를 통해 힙에 메모리를 동적으로 할당받습니다. 자바에서는 명시적으로 메모리를 해제할 필요가 없으며, 가비지 컬렉터가 더 이상 사용되지 않는 객체를 자동으로 해제합니다. 하지만, 개발자가 객체 참조를 올바르게 관리하지 않으면 여전히 메모리 누수 문제가 발생할 수 있습니다. 예를 들어, 사용하지 않는 객체에 대한 참조를 계속 유지하면 가비지 컬렉터가 해당 객체를 해제하지 못하므로 메모리 누수가 발생할 수 있습니다.

### 예시 코드: 메모리 누수 발생 상황

```java
import java.util.ArrayList;
import java.util.List;

public class MemoryLeakExample {
    // 클래스 필드로 큰 객체를 참조하는 리스트를 선언
    private static List<byte[]> memoryLeakList = new ArrayList<>();

    public static void main(String[] args) {
        for (int i = 0; i < 10000; i++) {
            byte[] largeArray = new byte[1024 * 1024]; // 1MB 크기의 배열 생성
            memoryLeakList.add(largeArray); // 배열을 리스트에 추가
            System.out.println("Iteration: " + i);
            // 여기서 largeArray에 대한 참조를 유지하고 있으므로, 가비지 컬렉션이 수행되지 않음
        }
    }
}
```

### 설명

이 예제에서 `memoryLeakList`는 클래스 필드로 선언된 정적 리스트입니다. 이 리스트는 `main` 메서드에서 매번 1MB 크기의 바이트 배열을 생성하고 해당 배열을 리스트에 추가하고 있습니다. 

- `memoryLeakList.add(largeArray);` 코드 줄이 계속해서 새로운 배열을 리스트에 추가함으로써, 메모리 사용량이 증가하게 됩니다.
- `largeArray`에 대한 참조가 계속 유지되기 때문에, 가비지 컬렉터는 이 배열들을 해제하지 못합니다.
- 결국, 메모리 누수가 발생하여 프로그램이 비정상적으로 종료되거나 메모리 부족 오류가 발생할 수 있습니다.

## 순환 그래프에서 모든 사이클을 탐지하는 DFS 알고리즘

순환 그래프에서 사이클을 탐지하기 위해 DFS를 사용할 수 있습니다. DFS를 수행하면서 방문한 노드를 추적하고, 이미 방문한 노드에 다시 도달했을 때 사이클이 존재한다고 판단할 수 있습니다. 이를 위해 방문 기록을 유지하고, 현재 탐색 중인 노드의 경로를 저장합니다.

## 재귀적 백트래킹에서의 'Combinatorial Explosion' 문제 해결 전략

- **가지치기(Pruning):** 유망하지 않은 경로를 미리 차단하여 탐색 공간을 줄입니다.
- **메모이제이션:** 이미 탐색한 경로의 결과를 저장하여 동일한 경로를 중복 탐색하지 않도록 합니다.
- **문제 크기 축소:** 문제의 입력 크기를 줄이거나 최적화 알고리즘을 적용하여 해결합니다.

## DFS를 사용하는 것이 BFS보다 유리한 경우

DFS는 공간 복잡도가 상대적으로 낮아야 할 때 유리합니다. 예를 들어, 깊이가 깊고 넓이가 좁은 그래프를 탐색할 때 BFS는 큐에 많은 노드를 저장해야 하므로 메모리 사용량이 많아질 수 있습니다. 반면 DFS는 스택에 깊이만큼의 노드만 저장하면 되므로 메모리 사용량이 적습니다.

---

## 실전 문제

### 문제 1: 피보나치 수열 계산

#### 설명
n번째 피보나치 수를 계산하세요. 피보나치 수열은 다음과 같은 방식으로 정의됩니다:

- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2), n ≥ 2

#### 입력
- 정수 n (0 ≤ n ≤ 40)

#### 출력
- n번째 피보나치 수를 출력합니다.

#### 예제 입력
```
5
```

#### 예제 출력
```
5
```

#### 예제 설명
5번째 피보나치 수는 5입니다. (수열: 0, 1, 1, 2, 3, 5)

---

### 문제 2: 이진 트리의 최대 깊이 찾기

#### 설명
이진 트리의 최대 깊이를 계산하세요. 최대 깊이는 루트 노드에서 가장 깊숙한 리프 노드까지의 경로 길이입니다.

#### 입력
- 이진 트리 노드의 수 n (0 ≤ n ≤ 1000)
- 노드 정보는 간선의 형식으로 주어집니다. 각 노드는 자식 노드와 연결될 수 있습니다.

#### 출력
- 트리의 최대 깊이를 출력합니다.

#### 예제 입력
```
1 2
1 3
2 4
2 5
```

#### 예제 출력
```
3
```

#### 예제 설명
트리는 루트 노드 1을 기준으로 깊이 3을 가집니다. (1 → 2 → 4 또는 1 → 2 → 5)

---

### 문제 3: 방향성 그래프에서 경로 탐색

#### 설명
주어진 방향성 그래프에서 시작 노드에서 끝 노드까지의 경로가 있는지 확인하세요.

#### 입력
- 정점의 수 n (1 ≤ n ≤ 1000)
- 간선의 수 m (1 ≤ m ≤ 5000)
- 각 간선은 두 정점 u와 v로 구성되어 있으며, u에서 v로의 단방향 경로를 나타냅니다.
- 마지막 줄에 시작 노드와 끝 노드가 주어집니다.

#### 출력
- 경로가 존재하면 "Yes", 존재하지 않으면 "No"를 출력합니다.

#### 예제 입력
```
4 4
1 2
2 3
3 4
4 2
1 4
```

#### 예제 출력
```
Yes
```

#### 예제 설명
정점 1에서 시작하여 정점 4까지 도달하는 경로가 존재합니다. (1 → 2 → 3 → 4)
