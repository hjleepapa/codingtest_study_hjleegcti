질문

큐를 이용하여 주어진 데이터를 순차적으로 처리하는 알고리즘을 설계하고 구현하세요. 이 알고리즘의 시간 복잡도는 어떻게 되나요? 큐를 사용하지 않고도 데이터를 순차적으로 처리할 수 있는 다른 방법을 설명하세요.

​

from collections import deque

class Queue: # FIFO. A, B, C 순서대로 입력되고 또 A,B,C 순서대로 출력된다. time complexity: O(1)
    def __init__(self):
        self._elements = deque()
    
    def enqueue(self, element):
        self._elements.append(element)
        
    def dequeue(self):
        return self._elements.popleft()
        

fifo = Queue()
fifo.enqueue("A")
fifo.enqueue("B")
fifo.enqueue("c")

print(fifo.dequeue()) => A
print(fifo.dequeue()) => B
print(fifo.dequeue()) => C

Queue나 deque를 사용하지 않고 데이타를 순차적으로 처리하는 방법은 list를 이용해서 다음처럼 시용하면 된다.
push() => append()
popleft() => pop(0)

그런데 pop(0)는 pop() 이나 popleft()보다 상당히 느린데 그 이유를 생각해 보면 맨앞의 것을 제거하고 전부 한칸씩 앞으로 옮겨줘야 하므로 
맨뒤의 것을 제거하는 pop()이나 맨앞의 것을 바로 제거하고 그대로 유지하는 popleft()보다 느리다는 것을 알수 있다.


​

2. 주어진 문자열에서 연속된 중복된 문자를 제거한 새로운 문자열을 반환하는 알고리즘을 설계하고 구현하세요. 단, 문자열 내에서 문자의 순서는 유지해야 합니다. 시간 복잡도를 분석하세요.

​

def solution(s): # TC: O(n), n is the length of string.
    
    q = []
    
    for i in range(len(s) - 1):
        q.append(s[i])
        
        if len(q) < 2:
            continue
        
        elif q[-1] == q[-2]:
            q.pop()
    
    return "".join(q)
    
print(solution("abbbccdeee"))
=> abcde
​

3. 큐와 스택의 차이점을 설명하고, 각각의 자료구조가 적합한 상황을 예시와 함께 설명해보세요. 두 자료구조의 시간 복잡도에 대한 일반적인 차이도 설명하세요.

stack: LIFO(Last In, First Out)
Queue: FIFO(First In, First Out)

stack: push & pop: data added to top and removed from top
Queue: enqueue & dequeue: data added to rear but removed from front

stack: 괄호짝 맞추기, DFS algorithm, reverse string, function call, etc.
queue: buffer management, scheduling, BFS algorithm, cache, etc


from collections import deque 

def solution(s):
    stack = []
    queue = deque()
    
    res_stack = []
    res_queue = []
    
    for i in range(len(s)):
        stack.append(s[i])
        queue.append(s[i])
        
    for _ in range(len(s)):
        res_stack.append(stack.pop())
        res_queue.append(queue.popleft())
    
    return (res_stack, res_queue)
    
print(solution("abcdefg"))
=> (['g', 'f', 'e', 'd', 'c', 'b', 'a'], ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

stack TC: push, pop, is_empty, top, size, etc. generally O(1). It uses only top. 
queue TC: enqueue, dequeue, is_empty, peek, etc. generally O(1), but it uses front and rear. 
so it needs to monitor always two points.
​

4. 큐를 이용하여 우선순위가 있는 작업을 처리하는 방법에 대해 설명하세요. 우선순위가 높은 작업을 먼저 처리할 수 있는 자료구조의 동작 원리와 그에 따른 시간 복잡도를 설명해보세요.

​

큐는 먼저 집어넣은 것이 먼저 나오는 구조인 선형자료구조이나, 우선순위 큐는 들어간 순서가 아니라 우선순위가 높은 것이 먼저 나오는 자료구조. 

​

        top priority

           ↓ 

Dequeue ←  9  7  5  3  1 ← Enqueue

          → Decreasing priority order

​

5 -> 9 ->7 순서로 데이타가 들어가는 경우, 우선순위큐는 9->7->5.

​

<우선순위 큐의 기본 동작>

​

enqueue() - add new value

1. enqueue 수행시 우선순위 순서를 유지하도록 구현하는 경우. 

새로운 데이타 추가시 우선순위에 맞는 위치에 삽이해 큐가 정렬된 상태를 유지. 

이경우 dequeue연산이 간단해서 첫번째 값이 가장 우선순위가 높아 O(1)의 TC를 가지나 반면 enqueue 연산이 비효율적이 되서 우선순위를 고려한 적절한 위치를 찾기 위해 데이터 우선순위를 검사해야 되므로 O(N)의 시간복잡도를 가진다.

​

​

​

dequeue() - remove the top priority value and return it

2. dequeue수행시 우선순위 우선순위가 높은 것을 선택하도록 구현하는 경우. 

새로운 데이타 추가시 그 값을 큐의 끝에 추가하고 연산이 일어날때 큐 내에서 우선순위가 가장 높은값을 찾는 방법.

enqueue연산이 간단해서 새로운 데이타 원소는 항상 큐의 끝에 추가되므로, O(1).

반면 dequeue연산이 비효율적으로 우선순위가 가장 높은 요소를 찾기 위해 큐의 모든 값을 검사해야 하므로 O(N). 

​

따라서 두 방식중 어떤것이 더 효율적인지는 각 연산의 빈번도가 어느것이 많으냐에 따라 알맞은 것을 선택.

​

peek() - return the top priority value

​

​

<우선순위 큐의 구현방식과 TC>

​

                      enqueue()        dequeue()

unsorted array          O(1)              O(N)

unsorted linked list    O(1)              O(N)

sorted array            O(N)              O(1)

sorted linked list      O(N)              O(1)

heap                    O(logN)           O(logN)


이처럼 heap이 평균적으로 O(logN)을 보장하므로 통상 힙을 가지고 구현을 함.

​

구현시 선형배열과 연결리스트를 사용할 수 있는데, 공간적 측면과 시간적 측면을 나눠 생각해 보자.

<공간적 측면>

선형배열: 메모리 공간을 연속적으로 사용하므로 메모리 공간을 효율적으로 사용 가능.

양방향연결리스트: 각 노드는 에이터와 앞노드와 뒤 노드를 가리키는 링트를 가지고 있어 추가적인 메모리 필요

​

<시간적 측면>

선형배열: 배열의 삽입/삭제는 인덱싱의 이동을 동반하므로 탐색과정을 고려하지 않아도 O(N)

양방향연결리스트: 링크의 재구성만이 이뤄지므로 삽입과 탐색과정을 고려하지 않았을때 O(1)

​

​

​

​==========================================================================================================================

​

실전 문제

문제 1: BFS(너비 우선 탐색) 알고리즘 구현

주어진 그래프에서 시작 노드부터 목표 노드까지의 최단 경로를 찾는 BFS 알고리즘을 큐를 이용하여 구현하세요.

입력: 그래프와 시작 노드, 목표 노드가 주어집니다.

출력: 시작 노드부터 목표 노드까지의 최단 경로를 리스트로 출력합니다.

예시 입력/출력

# 예시 입력 1 graph = { 'A' : ['B', 'C'], 'B' : ['A', 'D', 'E'], 'C' : ['A', 'F'], 'D' : ['B'], 'E' : ['B', 'F'], 'F' : ['C', 'E'] } start = 'A' goal = 'F' # 예시 출력 1 ['A', 'C', 'F']

입출력 설명

예시 1에서는 'A'에서 'F'까지 가는 최단 경로는 ['A', 'C', 'F']입니다.

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}


from collections import deque

def bfs(start, goal, graph):
    q = deque([start])
      
    while q:
        path = q.popleft()
        node = path[-1]
       
        if node == goal:
            return path
           
        for adj in graph[node]:
            new_path = list(path)
            new_path.append(adj)
            q.append(new_path)
           
start = 'A'
goal = 'F'

print(bfs(start, goal, graph))


문제 2: 캐시 구현

주어진 요청을 처리하는 간단한 캐시 시스템을 큐를 이용하여 구현하세요. 캐시는 고정된 크기를 가지며, 새로운 데이터가 들어올 때 공간이 부족하면 가장 오래된 데이터를 제거합니다.

입력: 캐시 크기와 요청 리스트가 주어집니다.

출력: 각 요청이 처리될 때마다 캐시의 상태를 출력합니다.

예시 입력/출력

# 예시 입력 1 cache_size = 3 requests = [1, 2, 3, 4, 1, 2, 5] # 예시 출력 1 [1] [1, 2] [1, 2, 3] [2, 3, 4] [3, 4, 1] [4, 1, 2] [1, 2, 5]

입출력 설명

예시 1에서는 캐시 크기가 3이므로, 공간이 부족하면 가장 오래된 요청을 제거하고 새로운 요청을 처리합니다.

from collections import deque
    
def solution(cache_size, requests):
    
    def lru_cache(n):
        
        if len(cache) >= cache_size:
            cache.popleft()
            cache.append(n)
        else:
            cache.append(n)
        
        return cache
    
    cache = deque()
    for request in requests:
        lru_cache(request)
        print(cache)
        
        
cache_size = 3
requests = [1, 2, 3, 4, 1, 2, 5]

print(solution(cache_size, requests))


문제 3: 우선순위 큐 구현

우선순위가 부여된 작업을 처리하는 우선순위 큐를 구현하세요. 우선순위가 높은 작업이 먼저 처리되며, 같은 우선순위를 가진 작업들은 먼저 들어온 순서대로 처리됩니다.

입력: 작업 목록과 각 작업의 우선순위가 주어집니다.

출력: 우선순위에 따라 작업을 처리한 순서대로 출력합니다.

예시 입력/출력

# 예시 입력 1 tasks = [(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D')] # 예시 출력 1 ['Task B', 'Task D', 'Task C', 'Task A']

입출력 설명

예시 1에서는 우선순위가 1인 'Task B'와 'Task D'가 먼저 처리되며, 같은 우선순위 내에서는 먼저 입력된 'Task B'가 먼저 처리됩니다.

​

tasks = [(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D'), (1, 'Task E'), (2, 'Task F')]

import heapq

def sol(tasks):
    res = []
    n = len(tasks)
    hq = []
    for i in range(n):
        heapq.heappush(hq, (tasks[i][0], i, tasks[i][1]))
    
    for i in range(n):
        seq, idx, task_id = heapq.heappop(hq)
        res.append(task_id)
    return res

print(sol(tasks))
​

​

문제 4: 최대 슬라이딩 윈도우

주어진 배열에서 슬라이딩 윈도우 방식으로 최대 값을 구하는 문제입니다. 윈도우의 크기 k가 주어졌을 때, 배열에서 k개의 연속된 숫자 중 가장 큰 숫자를 찾으세요.

입력: 배열과 윈도우 크기 k가 주어집니다.

출력: 각 윈도우에서의 최대 값을 리스트로 출력합니다.

예시 입력/출력

# 예시 입력 1 arr = [1, 3, -1, -3, 5, 3, 6, 7] k = 3 # 예시 출력 1 [3, 3, 5, 5, 6, 7]

입출력 설명

예시 1에서는 윈도우 크기가 3일 때, 각 슬라이딩 윈도우에서의 최대 값은 [3, 3, 5, 5, 6, 7]입니다.

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3 

import heapq

def sol(arr, k):
    res = []
    n = len(arr)
    hq = []
    for i in range(n-k+1):
        for j in range(i,i+k):
            heapq.heappush(hq, -arr[j])
        mx = heapq.heappop(hq)
        res.append(-mx)
        
    return res

print(sol(arr, k))
​
