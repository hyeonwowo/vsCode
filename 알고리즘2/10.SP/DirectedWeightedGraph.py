from pathlib import Path
from queue import PriorityQueue
from queue import Queue
import timeit

class DirectedEdge: # 방향 가중치 간선 클래스
    def __init__(self, v, w, weight): # Create an edge v->w with a double weight
        self.v, self.w, self.weight = v, w, weight
    
    def __lt__(self, other): # < operator, used to sort elements (e.g., in a PriorityQueue, sorted() function)
        assert(isinstance(other, DirectedEdge))
        return self.weight < other.weight

    def __gt__(self, other): # > operator, used to sort elements
        assert(isinstance(other, DirectedEdge))
        return self.weight > other.weight

    def __eq__(self, other): # == operator, used to compare edges for grading
        if other == None: return False
        assert(isinstance(other, DirectedEdge))
        return self.v == other.v and self.w == other.w and self.weight == other.weight

    def __str__(self): # Called when an Edge instance is printed (e.g., print(e))
        return f"{self.v}->{self.w} ({self.weight})"

    def __repr__(self): # Called when an Edge instance is printed as an element of a list
        return self.__str__()    


'''
Class for storing Weighted Digraphs
'''
class EdgeWeightedDigraph:
    def __init__(self, V): # Vertex 수를 고정하고 시작
        self.V = V # 정점 수
        self.E = 0 # 간선 수
        self.adj = [[] for _ in range(V)]   # adj[v] is a list of vertices adjacent to v
        self.edges = []

    def addEdge(self, v, w, weight): # Add edge v->w. Self-loops and parallel edges are allowed
        e = DirectedEdge(v, w, weight) # Create one edge instance and use it for adj[v], adj[w], and edges[]
        self.adj[v].append(e)        
        self.edges.append(e)
        self.E += 1
    
    def outDegree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for e in self.adj[v]: rtList.append(f"{e}\n")
        return "".join(rtList)

    def negate(self): # return an EdgeWeightedDigraph with all edge weights negated
        g = EdgeWeightedDigraph(self.V)
        for e in self.edges: g.addEdge(e.v, e.w, -e.weight)
        return g

    def reverse(self): # return an EdgeWeightedDigraph with all edges reversed
        g = EdgeWeightedDigraph(self.V)
        for e in self.edges: g.addEdge(e.w, e.v, e.weight)
        return g

    '''
    Create an EdgeWeightedDigraph from a file
        fileName: Name of the file that contains graph information as follows:
            (1) the number of vertices, followed by
            (2) one edge in each line, where an edge v->w with weight is represented by "v w weight"
            e.g., the following file represents a digraph with 3 vertices and 2 edges
            3
            0 1 0.12
            2 0 0.26
        The file needs to be in the same directory as the current .py file
    '''
    @staticmethod
    def fromFile(fileName):
        filePath = Path(__file__).with_name(fileName)   # Use the location of the current .py file   
        with filePath.open('r') as f:
            phase = 0
            line = f.readline().strip() # Read a line, while removing preceding and trailing whitespaces
            while line:                                
                if len(line) > 0:
                    if phase == 0: # Read V, the number of vertices
                        g = EdgeWeightedDigraph(int(line))
                        phase = 1
                    elif phase == 1: # Read edges
                        edge = line.split()
                        if len(edge) != 3: raise Exception(f"Invalid edge format found in {line}")
                        g.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))                        
                line = f.readline().strip()
        return g


'''
Min Priority Queue based on a binary heap 
    with decreaseKey operation added
'''
class IndexMinPQ:
    def __init__(self, maxN):
        if maxN < 0: raise Exception("maxN < 0")
        self.maxN = maxN                     # 저장 가능한 최대 index 수 (0 ~ maxN-1)
        self.n = 0                           # 현재 PQ에 들어있는 원소 수
        self.keys = [None] * (maxN + 1)      # 각 index에 대응되는 key값 저장 (index -> key)
        self.pq = [-1] * (maxN + 1)          # 힙 구조: pq[i] = index, i는 힙에서의 위치
        self.qp = [-1] * maxN                # 역관계: qp[index] = i (힙에서의 위치)
        # ⇒ 항상 pq[qp[i]] == i, qp[pq[i]] == i 성립

    def isEmpty(self):
        return self.n == 0                   # PQ가 비었는지 여부

    def contains(self, i):
        self.validateIndex(i)
        return self.qp[i] != -1              # index i가 현재 PQ에 존재하는지 여부

    def size(self):
        return self.n                        # 현재 PQ에 들어있는 원소 수 반환

    def insert(self, i, key):
        self.validateIndex(i)
        if self.contains(i): raise Exception(f"index {i} is already in PQ")
        self.n += 1
        self.qp[i] = self.n                  # index i는 힙의 self.n 위치에 들어감
        self.pq[self.n] = i                  # 힙의 self.n 위치에 index i 배정
        self.keys[i] = key                   # index i에 key 연결
        self.swimUp(self.n)                  # 힙 위로 정렬

    def minIndex(self):
        if self.n == 0: raise Exception("PQ has no element, so no min index exists")
        return self.pq[1]                    # 루트의 index 반환 (최소 key를 가진 index)

    def minKey(self):
        if self.n == 0: raise Exception("PQ has no element, so no min key exists")
        return self.keys[self.pq[1]]         # 루트의 key 반환 (최소 key)

    def delMin(self):
        if self.n == 0: raise Exception("PQ has no element, so no element to delete")
        minIndex = self.pq[1]                # 최소 key를 가진 index
        minKey = self.keys[minIndex]
        self.exch(1, self.n)                 # 루트와 마지막 원소 교환
        self.n -= 1                          # 힙 크기 감소
        self.sink(1)                         # 루트에서 아래로 정렬
        assert(minIndex == self.pq[self.n+1])
        self.qp[minIndex] = -1               # 해당 index는 PQ에서 제거됨을 표시
        self.keys[minIndex] = None
        self.pq[self.n+1] = -1               # 더 이상 사용되지 않음
        return minKey, minIndex              # 최소 key와 index 반환

    def keyOf(self, i):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        return self.keys[i]                  # index i의 key 반환

    def changeKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        self.keys[i] = key                   # key 갱신
        self.swimUp(self.qp[i])              # 위로 정렬
        self.sink(self.qp[i])                # 아래로 정렬 (양방향 가능성 고려)

    def decreaseKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        if self.keys[i] == key: raise Exception("new key is same as current key")
        if self.keys[i] < key: raise Exception("new key is greater than current key")
        self.keys[i] = key
        self.swimUp(self.qp[i])              # 키가 줄었으므로 위로만 정렬

    def increaseKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        if self.keys[i] == key: raise Exception("new key is same as current key")
        if self.keys[i] > key: raise Exception("new key is less than current key")
        self.keys[i] = key
        self.sink(self.qp[i])                # 키가 커졌으므로 아래로만 정렬

    def delete(self, i):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        idx = self.qp[i]                     # 힙에서의 위치
        self.exch(idx, self.n)               # 마지막 원소와 교환
        self.n -= 1
        self.swimUp(idx)                     # 교환 후 위로 정렬
        self.sink(idx)                       # 아래로도 정렬
        self.keys[i] = None
        self.qp[i] = -1                      # index 제거 표시

    def validateIndex(self, i):
        if i < 0: raise Exception(f"index {i} < 0")
        if i >= self.maxN: raise Exception(f"index {i} >= capacity {self.maxN}")

    def greater(self, i, j):
        # 힙에서 i, j 위치의 key 비교
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        # 힙 위치 i, j의 index를 교환하고 qp도 함께 갱신
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swimUp(self, idx):
        # 힙에서 위로 올라가며 key 정렬
        while idx > 1 and self.greater(idx // 2, idx):
            self.exch(idx, idx // 2)
            idx = idx // 2

    def sink(self, idx):
        # 힙에서 아래로 내려가며 key 정렬
        while 2 * idx <= self.n:
            idxChild = 2 * idx
            if idxChild < self.n and self.greater(idxChild, idxChild + 1):
                idxChild += 1
            if not self.greater(idx, idxChild):
                break
            self.exch(idx, idxChild)
            idx = idxChild



'''
Perform the topological sort on a DAG g, while detecing any cycle
    If a cycle is found, return False
    Otherwise, return list of vertices in reverse DFS postorder
'''
def topologicalSortWithCycleDetection(g):
    def recur(v):        
        visited[v] = True
        verticesInRecurStack.add(v)
        for e in g.adj[v]:
            if e.w in verticesInRecurStack: # Edge found to a vertex in the recursive stack
                print("cycle detected on vertex", e.w)                
                return False 
            if not visited[e.w]: 
                if not recur(e.w): return False
        reverseList.append(v) # Add v to the stack if all adjacent vertices were visited
        verticesInRecurStack.remove(v)
        return True

    assert(isinstance(g, EdgeWeightedDigraph))
    visited = [False for _ in range(g.V)]
    reverseList = []
    verticesInRecurStack = set() # Initialize set before the first call of recur()
    for v in range(g.V): 
        if not visited[v]:
            #verticesInRecurStack = set() # Initialize set before the first call of recur()
            if not recur(v): # Return False if a cycle is detected                
                return None

    reverseList.reverse()
    return reverseList

'''
Class that finds and stores shortest paths from a single source    
'''
    
class SP:
    def __init__(self, g, s): # 최단거리탐색
        if not isinstance(g, EdgeWeightedDigraph): raise Exception(f"{g} is not an EdgeWeightedDigraph")
        self.g, self.s = g, s
        self.validateVertex(s)        
        self.edgeTo = [None] * g.V # edgeTo[w]: 현재 노드의 이전 노드
        self.distTo = [float('inf')] * g.V  # distTo[w]: 현재 노드까지의 최소 가중치합
        self.distTo[s] = 0 # 출발점 - 0으로 초기화

    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPathTo(v): raise Exception(f"no path exists to vertex {v}")
        path = []
        e = self.edgeTo[v] # 현재 노드 이전부터 시작 (a -> b -> c -> d -> e 라고 할 때 pathTo(e) : a -> b -> c -> d (시작점 제외 나머지 경로만 반환))
        while e != None:
            path.append(e)
            e = self.edgeTo[e.v]
        path.reverse()
        return path

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.distTo[v] < float('inf') # 가중치합이 무한대이면 아직 경로가 없고, 무한대보다 작으면 경로 존재

    def relax(self, e):
        assert(isinstance(e, DirectedEdge))        
        if self.distTo[e.w] > self.distTo[e.v] +  e.weight: # w까지의 기존 거리 (알려진 거리) > v까지의 기존 거리(v는 w의 전) + v-w 간선의 가중치
            self.distTo[e.w] = self.distTo[e.v] +  e.weight # 새롭게 확장될 w 거리 업데이트
            self.edgeTo[e.w] = e # 새롭게 확장된 w의 정보 업데이트 (e : v, w, weight)

    def validateVertex(self, v):
        if v<0 or v>=self.g.V: raise Exception(f"vertex {v} is not between 0 and {self.g.V-1}")


class DijkstraSP(SP): # 상위클래스 : SP
    def __init__(self, g, s):
        super().__init__(g, s) # super().__init__ : 상속클래스 DijkstraSP 에서, 상위클래스 SP __init__() 메서드 사용
        self.pq = IndexMinPQ(g.V) # indexedPQ 초기화 : indexedPQ에 정점(index)과, 해당 정점까지의 최소 가중치합(key) 저장
        self.pq.insert(s, 0) # insert(정점, 최소 가중치합)
        self.closed = [False] * g.V # 방문노드 표시 리스트 (다익스트라에선 한번이라도 방문한 노드를 두번다시 방문하지 않음)
        while not self.pq.isEmpty(): 
            dist, v = self.pq.delMin() # (최소 가중치합, 정점) 꺼내옴
            self.closed[v] = True # 최소 가중치합을 가진 vertex에 방문 -> 방문처리
            for e in self.g.adj[v]: # 해당 vertex 주변 vertex 가중치합 계산 및 업데이트
                if not self.closed[e.w]: self.relax(e) # 방문하지 않은 vertex만 업데이트 (방문한 vertex라면 건들이지 않음)

    def relax(self, e): # relax 발동 조건 : 방문하지 않은 노드 (closed[v] = False)
        assert(isinstance(e, DirectedEdge))        
        if self.distTo[e.w] > self.distTo[e.v] +  e.weight:
            self.distTo[e.w] = self.distTo[e.v] +  e.weight
            self.edgeTo[e.w] = e
            if self.pq.contains(e.w): self.pq.decreaseKey(e.w, self.distTo[e.w]) # 만약 pq에 존재한다면, 최소가중치합 갱신 (감소)
            else: self.pq.insert(e.w, self.distTo[e.w]) # 만약에 pq에 없다면, 새로 추가

class AcyclicSP(SP):
    def __init__(self, g, s):
        super().__init__(g, s) 
        tpOrder = topologicalSortWithCycleDetection(g) # tpOrder을 얻어옴
        assert(tpOrder != None)
        for v in tpOrder: # tpOrder순으로 정점 v 선정
           for e in self.g.adj[v]:
                self.relax(e) # 상위클래스 SP에 있는 relax 발동

class BellmanFordSP(SP):
    def __init__(self, g, s):
        super().__init__(g, s)
        self.q = Queue(maxsize=g.V) # 큐의 최대 사이즈 고정시키고 시작
        self.onQ = [False] * g.V # 어떤 v가 Queue 내부에 있는지 빠르게 확인
        self.q.put(s) # 시작점 queue에 삽입
        self.onQ[s] = True # queue에 존재하는 s를 True로 설정
        while self.q.qsize() > 0:  
            v = self.q.get() 
            self.onQ[v] = False # 어떤 v를 Queue에서 꺼냈으므로 False
            for e in self.g.adj[v]: # 꺼낸 v에서 갈 수 있는 모든 vertex 탐색
                self.relax(e)

    def relax(self, e):
        assert(isinstance(e, DirectedEdge))        
        if self.distTo[e.w] > self.distTo[e.v] +  e.weight:
            self.distTo[e.w] = self.distTo[e.v] +  e.weight
            self.edgeTo[e.w] = e
            if not self.onQ[e.w]: # queue에 없다면
                self.q.put(e.w) # queue에 삽입
                self.onQ[e.w] = True # queue에 존재하니 True


if __name__ == "__main__":
    e1 = DirectedEdge(2, 3, 0.1)
    e1a = DirectedEdge(2, 3, 0.1)
    e2 = DirectedEdge(3, 4, 0.9)
    e3 = DirectedEdge(7, 3, 0.2)
    print("e1, e1a, e2, e3", e1, e1a, e2, e3)
    print("e1 == e1a", e1 == e1a)
    print("e1 < e2", e1 < e2)
    print("e1 > e3", e1 > e3)
    print("e2 < e3", e2 < e3)
    print()

    g1 = EdgeWeightedDigraph(8)
    g1.addEdge(4, 5, 0.35)
    g1.addEdge(5, 4, 0.35)
    g1.addEdge(4, 7, 0.37)
    g1.addEdge(5, 7, 0.28)
    g1.addEdge(7, 5, 0.28)
    g1.addEdge(5, 1, 0.32)
    g1.addEdge(0, 4, 0.38)
    g1.addEdge(0, 2, 0.26)
    g1.addEdge(7, 3, 0.39)
    g1.addEdge(1, 3, 0.29)
    g1.addEdge(2, 7, 0.34)
    g1.addEdge(6, 2, 0.40)
    g1.addEdge(3, 6, 0.52)
    g1.addEdge(6, 0, 0.58)
    g1.addEdge(6, 4, 0.93)
    print(g1)
    print(g1.adj[0])       
    print(g1.adj[7])
    print()

    g8i = EdgeWeightedDigraph.fromFile("wdigraph8i.txt")
    print("g8i", g8i)
    print("dijkstraSP on g8i")
    sp8i = DijkstraSP(g8i, 0)
    for i in range(g8i.V):
        if sp8i.hasPathTo(i): print(i, sp8i.distTo[i], sp8i.pathTo(i))
        else: print(i, "no path exists")
    print()

    g8a = EdgeWeightedDigraph.fromFile("wdigraph8a.txt")    
    print("g8a", g8a)
    print("dijkstraSP on g8a")
    sp8a = DijkstraSP(g8a, 0)
    print(sp8a.distTo)
    print(sp8a.edgeTo)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    print("BellmanFordSP on g8a")
    sp8a = BellmanFordSP(g8a, 0)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    print("acyclicSP on g8a")
    sp8a = AcyclicSP(g8a, 4)
    print(sp8a.distTo)
    print(sp8a.edgeTo)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    g8bn = EdgeWeightedDigraph.fromFile("wdigraph8b.txt").negate()
    print("acyclicSP on -g8b for vertex 5 as the source to find longest paths")
    sp8bn = AcyclicSP(g8bn, 5)
    for i in range(g8bn.V):
        if sp8bn.hasPathTo(i): print(i, -sp8bn.distTo[i], sp8bn.pathTo(i))
        else: print(i, "no path exists")    
    print()
    
    g6n = EdgeWeightedDigraph.fromFile("wdigraph6n.txt")
    print("BellmanFordSP on g6n")
    sp6n = BellmanFordSP(g6n, 0)
    for i in range(g6n.V):
        if sp6n.hasPathTo(i): print(i, sp6n.distTo[i], sp6n.pathTo(i))
        else: print(i, "no path exists")    
    print()

    print("DijkstraSP on g6n")
    sp6nD = DijkstraSP(g6n, 0)
    for i in range(g6n.V):
        if sp6nD.hasPathTo(i): print(i, sp6nD.distTo[i], sp6nD.pathTo(i))
        else: print(i, "no path exists")    
    print()
