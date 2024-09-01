# 목차
0. 면접 질문
1. 재귀 함수에서 재귀 깊이를 줄이기 위한 방법
2. 함수 호출 스택에서의 메모리 누수 문제와 방지 방법
3. 스택 기반 메모리 관리와 힙 기반 메모리 관리 비교
4. 순환 그래프에서 모든 사이클을 탐지하는 DFS 알고리즘
5. 재귀적 백트래킹에서의 'Combinatorial Explosion' 문제 해결 전략
6. DFS를 사용하는 것이 BFS보다 유리한 경우
7. 실전 문제
    - 문제 1: 피보나치 수열 계산
    - 문제 2: 이진 트리의 최대 깊이 찾기
    - 문제 3: 방향성 그래프에서 경로 탐색
    - 문제 4: 효율적인 거듭제곱 계산
    - 문제 5: 최대 공약수(GCD) 계산
---


## 면접 질문

1. 재귀 함수에서 '재귀 깊이 제한'에 도달하지 않도록 최적화하는 일반적인 기법들은 무엇이며, 각각의 장단점에 대해 설명해 주세요.
2. 함수 호출 스택에서 발생할 수 있는 메모리 누수의 원인과 이를 방지하기 위한 프로그래밍 기법은 무엇이 있을까요?
3. 스택 기반 메모리 관리와 힙 기반 메모리 관리의 구조적 차이점과 각각의 메모리 관리 방식이 가지는 장단점에 대해 설명해 주세요.
4. 재귀적 백트래킹 알고리즘에서 발생할 수 있는 '조합 폭발 문제(Combinatorial Explosion)'를 효율적으로 해결하기 위한 전략에는 어떤 것들이 있나요?
5. 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS) 알고리즘의 메모리 사용 패턴과 시간 복잡도를 비교하고, DFS가 더 적합한 문제 유형에는 어떤 것들이 있는지 설명해 주세요.
6. 재귀 호출의 성능 최적화를 위한 꼬리 재귀 최적화(Tail Call Optimization)에 대해 설명해주세요.
7. 자바의 가비지 컬렉션(Garbage Collection) 메커니즘이 작동하는 원리를 설명하고, 가비지 컬렉터가 비효율적으로 작동하여 메모리 누수가 발생할 수 있는 시나리오를 예시와 함께 설명해 주세요.
8. 순환 그래프에서 모든 사이클을 탐지하기 위해 깊이 우선 탐색(DFS) 알고리즘을 사용할 때 고려해야 할 주요 요소와 이를 효과적으로 구현하기 위한 설계 원칙은 무엇인가요?
9. 이진 트리의 최대 깊이를 찾는 문제에서 재귀적 접근법과 반복적 접근법의 시간 및 공간 복잡도를 비교하고, 각 접근법이 적합한 상황을 예시와 함께 설명해 주세요.



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

재귀적 백트래킹은 모든 가능한 해를 탐색하는 과정에서 발생하는 'Combinatorial Explosion'(조합 폭발) 문제를 겪을 수 있습니다. 이는 탐색 공간이 기하급수적으로 증가하면서 처리 속도가 느려지고 메모리 사용이 증가하는 문제입니다. 이러한 문제를 해결하기 위한 몇 가지 주요 전략을 소개합니다.

### 1. 가지치기(Pruning)

가지치기(Pruning)는 유망하지 않은 경로를 미리 차단하여 탐색 공간을 줄이는 기법입니다. 탐색 과정에서 특정 조건을 만족하지 않는 경우 더 이상 진행하지 않고 그 경로를 배제하는 방식으로, 연산 시간을 크게 줄일 수 있습니다.

#### 예시 코드 1: N-Queens 문제에서 가지치기 (Java)

```java
import java.util.ArrayList;
import java.util.List;

public class NQueens {

    // n-Queens 문제를 해결하는 메소드
    public static List<int[]> solveNQueens(int n) {
        List<int[]> result = new ArrayList<>(); // 결과를 저장할 리스트
        int[] board = new int[n]; // 퀸의 위치를 저장할 배열 (인덱스: 행, 값: 열)
        solve(0, board, result, n); // 재귀적으로 퀸을 배치
        return result; // 가능한 모든 해를 반환
    }

    // 재귀적으로 퀸을 배치하는 메소드
    private static void solve(int row, int[] board, List<int[]> result, int n) {
        // 모든 행에 퀸을 배치한 경우 결과에 추가
        if (row == n) {
            result.add(board.clone()); // 배열을 복제해서 저장
            return;
        }

        // 현재 행(row)에 가능한 모든 열(col) 시도
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col)) { // 유효한 위치인지 검사
                board[row] = col; // 퀸 배치
                solve(row + 1, board, result, n); // 다음 행으로 이동
                board[row] = -1; // 백트랙킹: 현재 행의 퀸 위치를 초기화
            }
        }
    }

    // 현재 퀸의 배치가 유효한지 검사하는 메소드
    private static boolean isValid(int[] board, int row, int col) {
        // 현재까지의 행을 검사하여 같은 열이나 대각선에 퀸이 있는지 확인
        for (int i = 0; i < row; i++) {
            if (board[i] == col || Math.abs(board[i] - col) == row - i) {
                return false; // 같은 열 또는 대각선에 퀸이 있음
            }
        }
        return true; // 유효한 위치
    }

    // 메인 메소드: 예제 실행
    public static void main(String[] args) {
        List<int[]> solutions = solveNQueens(4); // 4-Queens 문제 해결
        for (int[] solution : solutions) {
            for (int col : solution) {
                System.out.print(col + " "); // 각 해의 퀸 위치 출력
            }
            System.out.println();
        }
    }
}
```

위 코드에서 `isValid` 메소드는 현재 보드 상태에서 퀸이 놓일 수 있는지를 검사하여 유망하지 않은 경로를 가지치기합니다. 이러한 가지치기 기법을 통해 N-Queens 문제의 탐색 공간을 효율적으로 줄일 수 있습니다.

### 2. 메모이제이션(Memoization)

메모이제이션은 이미 탐색한 경로의 결과를 저장하여 동일한 경로를 중복 탐색하지 않도록 하는 기법입니다. 이는 중복 계산을 피하고 성능을 향상시키는 데 도움이 됩니다.

#### 예시 코드 2: 피보나치 수열 계산에서 메모이제이션 사용 (Java)

```java
import java.util.HashMap;
import java.util.Map;

public class FibonacciMemoization {

    // 피보나치 수를 저장할 메모이제이션 맵
    private static Map<Integer, Integer> memo = new HashMap<>();

    // 피보나치 수를 계산하는 메소드
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n; // 기본 조건: 0 또는 1일 때 n을 반환
        }
        if (memo.containsKey(n)) {
            return memo.get(n); // 이미 계산된 값이 있으면 반환
        }

        // 피보나치 수를 재귀적으로 계산하고 메모이제이션에 저장
        int result = fibonacci(n - 1) + fibonacci(n - 2);
        memo.put(n, result);
        return result; // 결과 반환
    }

    // 메인 메소드: 예제 실행
    public static void main(String[] args) {
        int n = 10;
        System.out.println("Fibonacci of " + n + " is: " + fibonacci(n)); // 피보나치 결과 출력
    }
}
```

위 예시에서 `memo` 맵은 이전에 계산된 피보나치 수의 값을 저장하고, 이미 계산된 값이 있을 경우 재계산하지 않고 저장된 값을 사용합니다. 이를 통해 중복된 계산을 피하고 성능을 크게 향상시킬 수 있습니다.

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


### 문제 4: 효율적인 거듭제곱 계산

#### 설명
주어진 정수 `x`와 `n`에 대해 `x`의 `n`제곱을 효율적으로 계산하는 프로그램을 작성하세요. `x^n`을 구하기 위해 단순히 `x`를 `n`번 곱하는 것보다 더 효율적인 방법을 사용하세요. 

이 문제는 분할 정복을 사용하여 재귀적으로 해결할 수 있습니다.

#### 입력
- 두 개의 정수 `x`와 `n`이 주어집니다. (1 ≤ x ≤ 10, 0 ≤ n ≤ 1000)

#### 출력
- `x^n`의 결과를 출력합니다.

#### 예제 입력
```
2 10
```

#### 예제 출력
```
1024
```

#### 예제 설명
2의 10제곱은 1024입니다. 단순히 2를 10번 곱하는 것 대신, 분할 정복을 통해 효율적으로 계산할 수 있습니다.

### 힌트
- `n`이 짝수일 때: `x^n = (x^(n/2)) * (x^(n/2))`
- `n`이 홀수일 때: `x^n = x * (x^(n-1))`



### 문제 5: 최대 공약수(GCD) 계산

#### 설명
두 정수 `a`와 `b`의 최대 공약수(Greatest Common Divisor, GCD)를 유클리드 알고리즘을 사용하여 재귀적으로 계산하는 프로그램을 작성하세요. 최대 공약수는 두 수를 동시에 나눌 수 있는 가장 큰 수입니다.

유클리드 알고리즘은 다음과 같이 정의됩니다:

- `GCD(a, b) = GCD(b, a % b)` (단, `b ≠ 0`)
- `GCD(a, 0) = a`

#### 입력
- 두 개의 정수 `a`와 `b`가 주어집니다. (1 ≤ a, b ≤ 10,000)

#### 출력
- `a`와 `b`의 최대 공약수를 출력합니다.

#### 예제 입력
```
48 18
```

#### 예제 출력
```
6
```

#### 예제 설명
48과 18의 최대 공약수는 6입니다. 유클리드 알고리즘을 사용하여 이를 재귀적으로 구할 수 있습니다.

---


