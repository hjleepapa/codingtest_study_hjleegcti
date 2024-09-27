# Queue

**목차**

1. [질문](https://github.com/dremdeveloper/codingtest_study/blob/main/basic/queue.md#%EC%A7%88%EB%AC%B8)
2. [실전 문제](https://github.com/dremdeveloper/codingtest_study/blob/main/basic/queue.md#%EC%8B%A4%EC%A0%84-%EB%AC%B8%EC%A0%9C)

---

**질문**

1. 큐를 이용하여 주어진 데이터를 순차적으로 처리하는 알고리즘을 설계하고 구현하세요. 이 알고리즘의 시간 복잡도는 어떻게 되나요? 큐를 사용하지 않고도 데이터를 순차적으로 처리할 수 있는 다른 방법을 설명하세요.

```python
# real implementation 

def do(param1):
	#...
	#...
	#...
	return 
	
from collections import deque

def solve(params,queue:deque):
	
	while queue:
		data = queue.popleft()
		do(data)
```

```python
# another way
def do(param1):
	#...
	#...
	#...
	return 
	
for datum in data:
	print(do(datum))

```

시간 복잡도는 데이터 사이즈 N라고 할 때, $O(N \sup_{data \in D}{f(data)} )$ 가 나올 거 같습니다. 

2. 주어진 문자열에서 연속된 중복된 문자를 제거한 새로운 문자열을 반환하는 알고리즘을 설계하고 구현하세요. 단, 문자열 내에서 문자의 순서는 유지해야 합니다. 시간 복잡도를 분석하세요.

```python

from collections import deque

def withoutRepeatedString(In:str):
    tmp = deque([]) # deque가 아니라 []로 해도 상관없습니다. 
    
    for char in In:
        if len(tmp)==0 or tmp[-1] != char:
            tmp.append(char) # enqueue 
    
    return ''.join(tmp)

print(withoutRepeatedString('aabbccdd'))
        
    
```

3. 큐와 스택의 차이점을 설명하고, 각각의 자료구조가 적합한 상황을 예시와 함께 설명해보세요. 두 자료구조의 시간 복잡도에 대한 일반적인 차이도 설명하세요.

가장 큰 차이점 : FIFO(선입선출, 先入先出)), LIFO(후입선출,後入先出) 

공통점 : 데이터를 순서대로 저장을 합니다. 그리고 push, pop의 시간복잡도는 둘다 O(1)입니다. 

queue를 이용하는 경우 : 은행이나 맛집에서 줄 서거나, 디아블로 대기열, 들어온 순서대로 나가야만 하는 경우 

stack을 이용하는 경우 : 괄호 맞추기, undo, 후위표기식, 박스에서 물건을 뺄 때, 교수님이 채점할 때  

4. 큐를 이용하여 우선순위가 있는 작업을 처리하는 방법에 대해 설명하세요. 우선순위가 높은 작업을 먼저 처리할 수 있는 자료구조의 동작 원리와 그에 따른 시간 복잡도를 설명해보세요.

주어진 연산자$_1$ 에 우선순위에 따라 동작하는 큐를 ‘우선순위 큐’라고 부릅니다. 다른 말로는 heap이라고도 합니다. heap은 complete binary tree 구조로 되어있습니다. 우선순위 큐의 ADT는 크게 다음과 같습니다:

설명하기 앞서 간단한 것부터 정리하고자 합니다:

a. heap은 complete binary tree이므로 현재 노드 기준으로 child node가 왼쪽 → 오른쪽 순서로 생겨야 합니다.
b. Left = 2*current, Right = 2*current + 2 
c. Parent = current//2입니다. binary tree이므로 모든 노드에서 parent는 하나입니다. 

우리의 기본적인 철학은 arr를 추상적인 자료구조인 heap에 맞게 변화하는 겁니다. 여기서 index를 이용해서 heap 구조를 만드려고 합니다. 그러니 대략적으로 이렇게 됩니다. 우리가 사용할 것 0-index인데 shifting을 하듯이 1-index에서 기준으로 루트를 설정하지만, -1를 해준 상태로 List에 적용할 것입니다. 이는 코드를 보면 이해가 될 겁니다. 

- heappush
    
    heappush란 obj를 heap 구조를 유지한 채 priority queue에 넣는 메소드를 말합니다. 
    
    새로운 obj가 heap 배열 맨 뒤에 들어옵니다. (append) 
    
    이 길이를 기준으로(current = len(heap)) parent = current//2 를 계산해서 이를 비교하면서 parent와 계속 swap을 해주는 메소드입니다.  
    
    (
    
    비교에 대한 추가설명 : heap[current-1] < heap[parent-1], 
    
    1. 여기서 부등호의 방향은 상황에 따라 다를 수 있습니다. 큰 게 먼저냐, 작은 게 먼저냐. 
    2. current, parent값은 1-index지만, heap은 0-index 기반으로 구현했기에 -1을 빼주고 list에 접근합니다.
    
    ) 
    

- heappop
    
    heappop이란 현재 priority queue에서 가장 우선순위가 큰 obj를 제거하고, 다시 priority queue의 구조를 유지하도록 재구성을 해주는 메소드를 말합니다. 
    
    h1. 제일 위의 노드인 heap[0]와 제일 뒤에 있는 노드인 heap[-1]를 swap 해줍니다.
    
    h2. 그리고 제일 뒤에 있는 부분을 pop 해줍니다. pop한 값은 기록해서 return 해야 합니다. 
    
    h3. heap[-1] 값이 heap[0]가 되었습니다. 그런데 제일 뒤에 있는 걸 가져왔기 때문에 heap 구조가 무너졌습니다. 다시 heap 구조를 세워야합니다. 그러니 current = 0이 됩니다. 
    
    h4. 앞서 언급했듯이, Left = current * 2, Right = current * 2 + 1, 그리고 LeftNode, RightNode와 current 중에 가장 큰 것을 찾아야 합니다. 
    
    h5. 만약에 current가 제일 크다면 break, LeftNode나 RightNode가 크다면 swap 하고 current를 더 큰 쪽의 index로 바꾼 뒤에 다음 스텝으로 진행합니다. 
    
    h6. 그렇게 끝나면 h2에서 언급했듯이 기존의 루트값을 리턴하고 끝냅니다. 
    
    ![image-8](https://github.com/user-attachments/assets/d2c6f5f0-f966-49c6-af5a-c148d663140f)

    위 그림은 full binary tree의 예시입니다. 
    

1. 여기서 말하는 연산자란 수학에서 말하는 total order가 되어야 한다고 생각합니다. 만약에 partial order라고 해봅시다. heappop 이후에 heap 구조가 재구성되었다고 가정해봅시다. 그럼 재구성된 heap tree에서 root node의 left, right 둘중 하나는 incomparable하기 때문에 이후 heap 구조에 대한 모순이 생깁니다. 

---

**실전 문제**

**문제 1: BFS(너비 우선 탐색) 알고리즘 구현**

주어진 그래프에서 시작 노드부터 목표 노드까지의 최단 경로를 찾는 BFS 알고리즘을 큐를 이용하여 구현하세요.

- **입력**: 그래프와 시작 노드, 목표 노드가 주어집니다.
- **출력**: 시작 노드부터 목표 노드까지의 최단 경로를 리스트로 출력합니다.

**예시 입력/출력**

```
# 예시 입력 1
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}
start = 'A'
goal = 'F'

# 예시 출력 1
['A', 'C', 'F']
```

**입출력 설명**

- 예시 1에서는 'A'에서 'F'까지 가는 최단 경로는 ['A', 'C', 'F']입니다.

문제 1 - 풀이 

---

```python

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}

# graph = dict{key:value} str:str
# bfs 트리를 만들고 역추적 

VIS = dict(zip(graph.keys(), [''] * len(graph)))
from collections import deque

def bfs(start:str, goal:str):
    
    VIS[start] = '0' # end 
    deq = deque([start])   
    
    while(deq):
        
        cur = deq.popleft()
        if cur == goal:
            return 

        for nxt in graph[cur]:
            if VIS.get(nxt,'') == '':
                VIS[nxt] = cur
                deq.append(nxt)
    return 

def trackingFromGoaltoStart(start, goal):
    
    ret = deque([])
    
    ret.appendleft(goal)
    cur = goal
    
    while(VIS[cur]!='0'):
        cur = VIS[cur]
        ret.appendleft(cur)
    
    return ret 

start = 'A'
goal = 'F'
bfs(start, goal)
ret = trackingFromGoaltoStart(start, goal)
print(*ret)
	
```

해설 : 

BFS 알고리즘에 대한 설명 

```python
# normal implementation 

from collections import deque

graph = [[1,2,3], [0,2], [0,1], [0]] 
n = 4 # node number size 
VIS = [False] * n
def bfs(start):
	queue = deque([start])
	VIS[start] = True
	
	while queue:
		cur = queue.popleft()
		
		for nxtNode in graph[cur]
			if not VIS[nxtNode]:
				queue.append(nxtNode)
				VIS[nxtNode] = True 
		
	return 
```

- BFS 알고리즘의 정당성
    
    Lemma : If (u,v) is an edge, where bfs ordering bfs(u) < bfs(v), then dist(s,u) + 1   ≤ dist(s, v)
    
    로 갈음하겠습니다. 
    
- BFS 알고리즘의 시간복잡도
    
    naive하게 생각해봅시다. BFS는 dequeue된 vertex를 기준으로 그 vertex의 neighborhood를 전부 탐색합니다. 따라서 BFS의 시간복잡도는 O(V + E)가 됩니다. $E = \sum_{v \in V} |N(v)|$
    

추가정보 : 0-1 BFS 

0-1 BFS는 간선의 가중치가 0, 1인 그래프에서 BFS를 돌리는 방법을 이야기한다. 

왜 다르냐면, 현재 위치에서 0을 선택해서 target에 갈 수 있고, 1을 선택해서 target에 갈 수 있다고 하자. 

그럼, 0을 선택해서 가는 게 훨씬 유리할 것이다. shortest path 측면에서 생각해보면 그렇다. 

여기서 기존의 BFS와 약간 달라진다. 가중치가 0이면 enqueue를 할 때 front에 넣어야 하고, 가중치가 1이면 stack처럼 enqueue를 해야 한다. 

- 언제 쓰는가? :  엣지의 가중치가 0이거나 1인 그래프에서 가장 빠른 거리가 짧은 path를 구할 때 사용됩니다.

dijstra를 쓸 수도 있지만 시간복잡도에서 Dijstra O(Elog(V)) $(\because O(E) = O(\log(V^2)) = O(\log(V) )$but BFS O(V+E) 이므로 이 경우에는 dijstra보다 더 빠를 수도 있습니다. 

- 어떻게 구현하는가?

```python
from collections import deque

graph = [[[1,1],[2,0],[3,0]], [[0,1],[2,1]], [[0,0],[1,1]], [[0,0]] ] 
n = 4 # node number size 
VIS = [False] * n
DIST = [float('inf')] * n

def bfs(start, target): # 0-index
	queue = deque([start])
	DIST[start] = 0
	
	while queue:
		cur = queue.popleft()
		
		for nxtNode, weight in graph[cur] # node : [next_vertex, weight]
			if DIST[cur] + weight < DIST[nxtNode]:
				DIST[nxtNode] = DIST[cur] + weight
				if weight:
					queue.append(nxtNode)
				else:
					queue.appendleft(nxtNode) 
		
	return DIST[target]
```

아래 링크를 참고했습니다. 

[https://cp-algorithms.com/graph/01_bfs.html](https://cp-algorithms.com/graph/01_bfs.html)

**문제 2: 캐시 구현**

주어진 요청을 처리하는 간단한 캐시 시스템을 큐를 이용하여 구현하세요. 캐시는 고정된 크기를 가지며, 새로운 데이터가 들어올 때 공간이 부족하면 가장 오래된 데이터를 제거합니다.

- **입력**: 캐시 크기와 요청 리스트가 주어집니다.
- **출력**: 각 요청이 처리될 때마다 캐시의 상태를 출력합니다.

**예시 입력/출력**

```
# 예시 입력 1
cache_size = 3
requests = [1, 2, 3, 4, 1, 2, 5]

# 예시 출력 1
[1]
[1, 2]
[1, 2, 3]
[2, 3, 4]
[3, 4, 1]
[4, 1, 2]
[1, 2, 5]
```

**입출력 설명**

- 예시 1에서는 캐시 크기가 3이므로, 공간이 부족하면 가장 오래된 요청을 제거하고 새로운 요청을 처리합니다.

문제 2 풀이 

---

```python
cache_size = 3
requests = [1, 2, 3, 4, 1, 2, 5]

deq = deque([])

for request in requests:
    
    if len(deq) < 3:
        deq.append(request)
    else:
        deq.popleft()
        deq.append(request)
    print(list(deq))
```

해설  : 

queue를 이용했기 때문에 front 앞에 있는 게 제일 오래 queue에 있었던 요청임을 쉽게 알 수 있습니다. 

그러므로, 다른 요청을 넣어야 할 때 queue의 front를 지우고,( popleft() ) queue에 append를 할 수 있다. 

requests를 돌면서 cache 사이즈가 3보다 작을 땐 곧장 queue에 넣고

🚧 deque ≠ queue 

파이썬에서 queue가 직접적으로 구현된 built-in library는 없습니다. 

deque를 이용해서 해야 합니다. deque는 queue + stack으로 이해하면 간단합니다. 

양방향으로 pop, push를 O(1) 비용으로 할 수 있는 자료구조입니다. 

그럼 이렇게 물어볼 수 있습니다. “deque가 queue나 stack 보다 상위 자료구조(?)인데 왜 queue나 stack을 쓸까요? 항상 deque를 쓰면 되잖아요.”

이 질문에 대한 대답은 아래의 stack-over-flow에서 가져왔습니다. 

[When to prefer stack/queue over deque?](https://stackoverflow.com/questions/20257128/when-to-prefer-stack-queue-over-deque)

“They are designed to prevent certain operations that would be allowable on a `deque`, such as adding or removing an element in the middle, or even iterating through the container. Such operations are totally unacceptable in a strict stack or queue implementation.”

요약해서 번역하자면, deque가 아니라 queue, stack을 쓰는 본질적인 이유는 deque에서 존재하는 기능을 아예 쓰지 못하도록 원천봉쇄하기 위함입니다. 

**“You might think it's fine** to use a `deque` because *you* know that you intended to use it as a normal queue. But when somebody else comes along a few years later and your project has grown significantly, **it might not be at all obvious to that person**. Doing a non-queue operation *just because they can* to hack around some other issue, your program may inadvertently be broken in subtle ways that could go undetected for weeks, months or years.”

왜냐하면 다른 사람이 논리를 이해하지 못하고, 전혀 다른 방향으로 수정해서 여러 문제들을 만들기 때문입니다.

priority queue를 이용한 LRU 버전 

LRU란? Least-recently-used algorithm은 큐 안에 있는 것 중에 가장 오래 전에 참조한 것을 먼저 제거하는 알고리즘입니다. 이는 cache hit의 효율을 더 좋게 하기 위함입니다. 대신 아래 코드에서도 보듯이 캐시사이즈가 커질 때 업데이트에 대한 오버헤드가 커짐을 알 수 있습니다. 

- 참고 문제 : 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시

                        [https://school.programmers.co.kr/learn/courses/30/lessons/17680](https://school.programmers.co.kr/learn/courses/30/lessons/17680) 

```java
// solution code for the above problem
// 참고만 하셔요.

import java.util.LinkedList;
import java.util.HashMap;

class Solution {

    LinkedList<Pair> list = new LinkedList<>();

    HashMap<String, Integer> check = new HashMap<String, Integer>();

    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0){
            return cities.length * 5;
        }

        int answer = 0;
        for(int i = 0;i< cities.length;i++){
            String city = cities[i].toUpperCase();
            if(check.getOrDefault(city,0) == 0){ // 큐에 city가 없을 때
                Pair tmp = new Pair(i+1, city);
                check.put(city, 1);
                if(list.size() >= cacheSize){ 
                    // 만약에 queue가 full 일 때 
                    // LRU 삭제 부분 
                    Pair lst = list.getLast();
                    check.remove(lst.city);
                    list.pollLast();
                }
                list.addFirst(tmp);   
                answer += 5;
            }else{
                // LRU 기록 부분 
                int k = 0;
                for(;k<list.size();k++){
                    if(city.equals(list.get(k).city)){
                        break;
                    }
                }
                Pair cur = list.get(k); 
                list.remove(k);
                list.addFirst(cur);
                answer+=1;
            }

        }
        return answer;
    }

    class Pair implements Comparable<Pair>{
        int time;
        String city;
        Pair(int time, String city){
            this.time = time;
            this.city = city;
        }

        @Override
        public int compareTo(Pair other){
            if(this.time != other.time){
                return Integer.compare(this.time, other.time);
            }else{
                return this.city.compareTo(other.city);
            }
        }
    }
}
```

**문제 3: 우선순위 큐 구현**

우선순위가 부여된 작업을 처리하는 우선순위 큐를 구현하세요. 우선순위가 높은 작업이 먼저 처리되며, 같은 우선순위를 가진 작업들은 먼저 들어온 순서대로 처리됩니다.

- **입력**: 작업 목록과 각 작업의 우선순위가 주어집니다.
- **출력**: 우선순위에 따라 작업을 처리한 순서대로 출력합니다.

**예시 입력/출력**

```
# 예시 입력 1
tasks = [(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D')]

# 예시 출력 1
['Task B', 'Task D', 'Task C', 'Task A']
```

**입출력 설명**

- 예시 1에서는 우선순위가 1인 'Task B'와 'Task D'가 먼저 처리되며, 같은 우선순위 내에서는 먼저 입력된 'Task B'가 먼저 처리됩니다.

문제 풀이 3 

---

```python
tasks = [(3, 'Task A'), (1, 'Task B'), (2, 'Task C'), (1, 'Task D')]
heap = []
# 예시 출력 1
['Task B', 'Task D', 'Task C', 'Task A']

# - **입력**: 작업 목록과 각 작업의 우선순위가 주어집니다. 
# - **출력**: 우선순위에 따라 작업을 처리한 순서대로 출력합니다.

# 우선순위란 작은 숫자 우선 -> 작은 문자 우선 
# 전처리 먼저 
# 그 뒤에 pq 구현 

def preprocess(tasks):
    ret = [] 
    for task in tasks:
        ret.append((task[0], task[1][-1]))
    return ret 

# q : heap index must start from idx = 1 ? 
def heappush(obj):

    heap.append(obj)
    current = len(heap) # 1부터 
    while current > 1:
        parent = (current)//2 # 1-index 
        # if parent == 0:
        print(current, parent, heap[0], heap[1])
        if heap[current-1] < heap[parent-1]:
            heap[current-1], heap[parent-1] = heap[parent-1], heap[current-1]
            current = parent
        # elif heap[current-1][0] == heap[parent][0]:
        #     if heap[current-1][1] < heap[parent][1]:
        #         heap[current-1], heap[parent-1] = heap[parent], heap[current]
        #         current = parent
        #     else:
        #         break
        else:
            break
    return 

def heappop():
    if not heap:
        return
    
    heap[0], heap[-1] = heap[-1], heap[0]
    min_item = heap.pop()
    current = 1
    while True:
        Left = 2*current
        Right = 2*current + 1
        print(Left,Right)
        smallest = current 
        if Left <= len(heap) and  heap[smallest-1] > heap[Left-1]:
            smallest = Left

        if Right <= len(heap) and heap[smallest-1] > heap[Right-1]:
            smallest = Right
                
        if smallest != current:
            heap[smallest-1], heap[current-1] = heap[current-1], heap[smallest-1]
        else:
            break

    return min_item
        

tasks = preprocess(tasks)
for task in tasks: # ok 
    heappush(task)

st = []
while heap:
    cur = heappop()
    # print( (cur[0],"Task " + cur[1]),end=" ")
    st.append(cur)
print(st)
```

해설 : 

1. 전처리 먼저 : 전처리란? ‘Task A’, ‘Task B’를 비교하는데 있어서 string Task가 불필요하고 메모리만 잡아먹으니, ‘Task A’ → ‘A’, ‘Task B’ → ‘B’로 바꿔서 ‘A’, ‘B’를 비교합니다. 그 이후에 다시 되돌립니다. 
2. 결과를 보았을 때, 여기서의 우선순위란 1. 작은 숫자 우선, 만약에 같다면, 2. 먼저 오는 문자순. 
3. operation을 정의했으니, priority queue 구현 : heappush, heappop
4. heappop을 하면서 전처리했던 내용을 다시 되돌리기.

  

**문제 4: 최대 슬라이딩 윈도우**

주어진 배열에서 슬라이딩 윈도우 방식으로 최대 값을 구하는 문제입니다. 윈도우의 크기 k가 주어졌을 때, 배열에서 k개의 연속된 숫자 중 가장 큰 숫자를 찾으세요.

- **입력**: 배열과 윈도우 크기 k가 주어집니다.
- **출력**: 각 윈도우에서의 최대 값을 리스트로 출력합니다.

**예시 입력/출력**

```
# 예시 입력 1
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# 예시 출력 1
[3, 3, 5, 5, 6, 7]
```

**입출력 설명**

- 예시 1에서는 윈도우 크기가 3일 때, 각 슬라이딩 윈도우에서의 최대 값은 [3, 3, 5, 5, 6, 7]입니다.

```python
# **문제 4: 최대 슬라이딩 윈도우**
# 주어진 배열에서 슬라이딩 윈도우 방식으로 최대 값을 구하는 문제입니다. 
# 윈도우의 크기 k가 주어졌을 때, 배열에서 k개의 연속된 숫자 중 가장 큰 숫자를 찾으세요.
# - **입력**: 배열과 윈도우 크기 k가 주어집니다.
# - **출력**: 각 윈도우에서의 최대 값을 리스트로 출력합니다.
 

from collections import deque
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

def max_sliding_window(arr, k): # O(N)
    deq = deque([])
    ret = [] 
    for i in range(len(arr)):
        
        while deq and deq[0] < i - k + 1:
            # i - k + 1 란 것은 sliding window의 끝 idx를 i라고 할 때 시작 index = i - k + 1 
            # idx : 0 1 2 3 4 5 6 
            #         |    i
            #    시작 i - k + 1
            deq.popleft()
        
        # 만약에 현재값이 더 크면 ? 
        while deq and arr[deq[-1]] < arr[i]:
            deq.pop()
        
        deq.append(i) 
        
        if i >= k-1: # 0-index에서는 k-1부터 max값을 구할 수 있으니 
            ret.append(arr[deq[0]])
        
    return ret 

print(max_sliding_window(arr, 3))
	# [3, 3, 5, 5, 6, 7]
```

해설 : 

sliding window란 창문의 왼쪽 열고, 오른쪽을 닫을 때 창문의 크기가 유지가 되는 것처럼 큐를 특정 사이즈로 유지하면서 부분 배열을 탐색하는 기법을 말합니다. 

문제에서는 연속된 부분배열에서의 최댓값을 출력하길 원합니다. 그런데, naive하게 구현을 하면 모든 부분배열을 전부 탐색해야 합니다. 슬라이딩 윈도우로 구현을 하게 된다면 다시 되돌아가서 탐색할 필요 없이 for 문 한번으로 구하고자 하는 연속된 부분배열에서의 최댓값을 구할 수 있습니다.
