from pathlib import Path
from queue import PriorityQueue
import timeit

class Edge: # 간선 가중치 부여
    def __init__(self, v, w, weight): # Create an edge v-w with a double weight
        if v <= w: self.v, self.w = v, w  # Put the lesser number in v for convenience
        else: self.v, self.w = w, v        
        self.weight = weight
    
    def __lt__(self, other): # < operator, used to sort elements (e.g., in a PriorityQueue, sorted() function)
        assert(isinstance(other, Edge))
        return self.weight < other.weight

    def __gt__(self, other): # > operator, used to sort elements
        assert(isinstance(other, Edge))
        return self.weight > other.weight

    def __eq__(self, other): # == operator, used to compare edges for grading
        assert(isinstance(other, Edge))
        return self.v == other.v and self.w == other.w and self.weight == other.weight

    def __str__(self): # Called when an Edge instance is printed (e.g., print(e))
        return f"{self.v}-{self.w} ({self.weight})"

    def __repr__(self): # Called when an Edge instance is printed as an element of a list
        return self.__str__()

    def other(self, v): # Return the vertex on the Edge other than v
        if self.v == v: return self.w
        else: return self.v

class WUGraph: # 가중치 무방향 그래프
    def __init__(self, V): # Constructor
        self.V = V # Number of vertices
        self.E = 0 # Number of edges
        self.adj = [[] for _ in range(V)]   # adj[v] is a list of vertices adjacent to v
        self.edges = []

    def addEdge(self, v, w, weight): # Add edge v-w. Self-loops and parallel edges are allowed
        e = Edge(v, w, weight) # Create one edge instance and use it for adj[v], adj[w], and edges[]
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.edges.append(e)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for e in self.adj[v]:
                if v == e.v: rtList.append(f"{e}\n") # Do not print the same edge twice
        return "".join(rtList)

    '''
    Create a WUGraph instance from a file
        fileName: Name of the file that contains graph information as follows:
            (1) the number of vertices, followed by
            (2) one edge in each line, where an edge v-w with weight is represented by "v w weight"
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
                        g = WUGraph(int(line))
                        phase = 1
                    elif phase == 1: # Read edges
                        edge = line.split()
                        if len(edge) != 3: raise Exception(f"Invalid edge format found in {line}")
                        g.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))                        
                line = f.readline().strip()
        return g

'''
Class for performing Union Find using weighted quick union
    and storing the results    
'''
class UF: # Union-Find
    def __init__(self, V): # V: the number of vertices
        self.ids = [] # ids[i]: i's parent
        self.size = [] # size[i]: size of tree rooted at i
        for idx in range(V):
            self.ids.append(idx)
            self.size.append(1)       

    def root(self, i):
        while i != self.ids[i]: 
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):    
        id1, id2 = self.root(p), self.root(q)
        if id1 == id2: return
        if self.size[id1] <= self.size[id2]: 
            self.ids[id1] = id2
            self.size[id2] += self.size[id1]
        else:
            self.ids[id2] = id1
            self.size[id1] += self.size[id2]

'''
Min Priority Queue based on a binary heap 
    with decreaseKey operation added
'''
class IndexMinPQ:
    def __init__(self, maxN): # Create an indexed PQ with indices 0 to (N-1)
        if maxN < 0: raise Exception("maxN < 0")
        self.maxN = maxN # Max number of elements on PQ
        self.n = 0 # Number of elements on PQ
        self.keys = [None] * (maxN+1)  # keys[i]: key with index i
        self.pq = [-1] * (maxN+1)  # pq[i]: index of the key at heap position i (pq[0] is not used)        
        self.qp = [-1] * maxN # qp[i]: heap position of the key with index i (inverse of pq[])        

    def isEmpty(self):
        return self.n == 0

    def contains(self, i): # Is i an index on the PQ?
        self.validateIndex(i)
        return self.qp[i] != -1

    def size(self):
        return self.n

    def insert(self, i, key): # Associate key with index i
        self.validateIndex(i)
        if self.contains(i): raise Exception(f"index {i} is already in PQ")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swimUp(self.n)

    def minIndex(self): # Index associated with the minimum key
        if self.n == 0: raise Exception("PQ has no element, so no min index exists")
        return self.pq[1]

    def minKey(self):
        if self.n == 0: raise Exception("PQ has no element, so no min key exists")
        return self.keys[self.pq[1]]

    def delMin(self):
        if self.n == 0: raise Exception("PQ has no element, so no element to delete")
        minIndex = self.pq[1]
        minKey = self.keys[minIndex]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        assert(minIndex == self.pq[self.n+1])
        self.qp[minIndex] = -1 # Mark the index as being deleted
        self.keys[minIndex] = None
        self.pq[self.n+1] = -1
        return minKey, minIndex

    def keyOf(self, i):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        else: return self.keys[i]

    def changeKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        self.keys[i] = key
        self.swimUp(self.qp[i])
        self.sink(self.qp[i])

    def decreaseKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        if self.keys[i] == key: raise Exception(f"calling decreaseKey() with key {key} equal to the previous key")
        if self.keys[i] < key: raise Exception(f"calling decreaseKey() with key {key} greater than the previous key {self.keys[i]}")
        self.keys[i] = key
        self.swimUp(self.qp[i])

    def increaseKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        if self.keys[i] == key: raise Exception(f"calling increaseKey() with key {key} equal to the previous key")
        if self.keys[i] > key: raise Exception(f"calling increaseKey() with key {key} smaller than the previous key {self.keys[i]}")
        self.keys[i] = key
        self.sink(self.qp[i])

    def delete(self, i):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        idx = self.qp[i]
        self.exch(idx, self.n)
        self.n -= 1
        self.swimUp(idx)
        self.sink(idx)
        self.keys[i] = None
        self.qp[i] = -1   

    def validateIndex(self, i):
        if i < 0: raise Exception(f"index {i} < 0")
        if i >= self.maxN: raise Exception(f"index {i} >= capacity {self.maxN}")

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swimUp(self, idx): # idx is the index in pq[]
        while idx>1 and self.greater(idx//2, idx):
            self.exch(idx, idx//2)            
            idx = idx//2

    def sink(self, idx): # idx is the index in pq[]
        while 2*idx <= self.n:    # If a child exists
            idxChild = 2*idx # Left child
            if idxChild<self.n and self.greater(idxChild, idxChild+1): idxChild = idxChild+1 # Find the smaller child
            if not self.greater(idx, idxChild): break
            self.exch(idx, idxChild) # Swap with (i.e., sink to) the greater child
            idx = idxChild

'''
Find an MST (Minimum Spanning Tree) using Kruskal's algorithm
    and return the MST with its weight sum
'''
def mstKruskal(g): # Constructor: finds an MST and stores it
    assert(isinstance(g, WUGraph)) # 가중치 무방향 그래프
    
    edgesInMST = [] # MST 구성 간선 저장 리스트
    weightSum = 0 # 가중치 총합

    pq = PriorityQueue() # 최소 가중치 기준 오름차순 정렬
    for e in g.edges:
        pq.put(e) # 모든 간선 pq에 삽입

    uf = UF(g.V) # union-find 그룹에 vertex 추가
    while not pq.empty() and len(edgesInMST) < g.V-1: # pq에 간선이 더이상 없거나, 추가된 간선이 v-1개면 종료
        e = pq.get()
        if not uf.connected(e.v, e.w):
            uf.union(e.v, e.w)
            edgesInMST.append(e)
            weightSum += e.weight

    return edgesInMST, weightSum


'''
Find an MST (Minimum Spanning Tree) using Prim's algorithm (lazy version)
    and return the MST with its weight sum
'''
def mstPrimLazy(g):
    def include(v): # v를 MST에 추가 & 인접한 간선 중 MST 외부로 향하는 간선 모두 추가
        included[v] = True
        for e in g.adj[v]:            
            if not included[e.other(v)]: pq.put(e) # 반대 v가 MST에 포함되지 않은 경우에만 v-w 간선 (e) 추가

    assert(isinstance(g, WUGraph))

    edgesInMST = []
    included = [False] * g.V # MST 포함여부 확인 리스트
    weightSum = 0 
    pq = PriorityQueue()
    include(0)

    while not pq.empty() and len(edgesInMST) < g.V-1:
        e = pq.get()
        if included[e.v] and included[e.w]: continue # 최소 weight 간선 v-w를 Pop한 후 v,w모두 MST상에 있지 않다면 continue
        edgesInMST.append(e)
        weightSum += e.weight
        if not included[e.v]: include(e.v) # e.v가 아직 MST에 안들어가 있으면, MST에 추가하고 간선 확장
        if not included[e.w]: include(e.w) # e.w가 아직 MST에 안들어가 있으면, MST에 추가하고 간선 확장

    return edgesInMST, weightSum    


'''
Find an MST (Minimum Spanning Tree) using Prim's algorithm (eager version)
    and return the MST with its weight sum
'''
def mstPrimEager(g):    
    def include(i):
        included[i] = True
        for e in g.adj[i]:
            j = e.other(i)
            if included[j]: continue
            if not pq.contains(j):  # 아직 PQ에 없으면 삽입
                edgeTo[j] = e
                pq.insert(j, e)
            elif e.weight < edgeTo[j].weight:  # 더 짧은 간선이면 갱신
                edgeTo[j] = e
                pq.decreaseKey(j, e)

    assert isinstance(g, WUGraph)

    edgeInMST = []
    edgeWeightSum = 0
    included = [False for _ in range(g.V)]
    edgeTo = [None for _ in range(g.V)]  # 각 정점으로 연결되는 최소 간선
    pq = IndexMinPQ(g.V)

    include(0)

    while not pq.isEmpty() and len(edgeInMST) < g.V - 1:
        e, v = pq.delMin()  # 정점 v로 연결되는 최소 간선 e
        edgeInMST.append(e)
        edgeWeightSum += e.weight
        include(v)

    return edgeInMST, edgeWeightSum


if __name__ == "__main__":
    # Unit test for Edge and WUGraph
    e1 = Edge(2,3,0.1)
    e2 = Edge(2,3,0.1)
    e3 = Edge(2,3,0.2)
    print(e1 == e1)
    print(e1 == e2)
    print(e1 == e3)
    print(e1.other(3))
    print(e1.other(2))
    
    g8 = WUGraph.fromFile("wugraph8.txt")
    print(g8)


    # Unit test for the min PQ
    minPQ = IndexMinPQ(10)
    minPQ.insert(0,'P')
    print(minPQ.pq, minPQ.keys, minPQ.qp)
    minPQ.insert(1,'Q')
    print(minPQ.pq, minPQ.keys, minPQ.qp)
    minPQ.changeKey(0,'R')
    print(minPQ.pq, minPQ.keys, minPQ.qp)
    minPQ.insert(2,'E')
    minPQ.insert(3,'X')
    minPQ.insert(4,'A')
    minPQ.insert(5,'M')
    minPQ.insert(6,'P')
    minPQ.insert(7,'L')
    minPQ.insert(8,'E')
    print(minPQ.pq, minPQ.keys, minPQ.qp)
    print(minPQ.delMin())    
    print(minPQ.delMin())    
    print(minPQ.delMin())
    print(minPQ.delMin())
    print(minPQ.delMin())
    minPQ.decreaseKey(3,'B')
    print(minPQ.delMin())
    print(minPQ.delMin())
    print(minPQ.delMin())
    print(minPQ.delMin())    
    
    # Unit Test for mstPrimEager()
    g3 = WUGraph.fromFile("wugraph3.txt")    
    print("Kruskal on g3", mstKruskal(g3))    
    print("Prim lazy on g3", mstPrimLazy(g3))    
    print("Prim eager on g3", mstPrimEager(g3))
    edges, weightSum = mstPrimEager(g3)     
    if edges ==  [Edge(0, 1, 4), Edge(1, 2, 7)]: print ("pass")
    else: 
        print ("fail")        
    if weightSum == 11: print ("pass")
    else: 
        print ("fail")        
    print()

    g8a = WUGraph.fromFile("wugraph8a.txt")    
    print("Kruskal on g8a", mstKruskal(g8a))    
    print("Prim lazy on g8a", mstPrimLazy(g8a))    
    print("Prim eager on g8a", mstPrimEager(g8a))
    edges, weightSum = mstPrimEager(g8a)
    failCorrectness = False
    if weightSum == 50: print ("pass")
    else: 
        print ("fail")
        failCorrectness = True
    print()


    g8 = WUGraph.fromFile("wugraph8.txt")
    print("Kruskal on g8", mstKruskal(g8))    
    print("Prim lazy on g8", mstPrimLazy(g8))    
    print("Prim eager on g8", mstPrimEager(g8))
    edges, weightSum = mstPrimEager(g8)
    failCorrectness = False    
    if edges == [Edge(0, 7, 0.16), Edge(1, 7, 0.19), Edge(0, 2, 0.26), Edge(2, 3, 0.17), Edge(5, 7, 0.28), Edge(4, 5, 0.35), Edge(2, 6, 0.4)]: print ("pass")
    else: 
        print ("fail")
        failCorrectness = True
    if weightSum == 1.81: print ("pass")
    else: 
        print ("fail")
        failCorrectness = True
    print()
    

    g10 = WUGraph.fromFile("wugraph10.txt")    
    print("Kruskal on g10", mstKruskal(g10))    
    print("Prim lazy on g10", mstPrimLazy(g10))    
    print("Prim eager on g10", mstPrimEager(g10))
    edges, weightSum = mstPrimEager(g10)     
    if edges ==  [Edge(0, 6, 0.39), Edge(0, 7, 0.73), Edge(3, 7, 0.38), Edge(3, 9, 0.17), Edge(1, 9, 0.47), Edge(1, 2, 0.08),\
         Edge(1, 5, 0.48), Edge(3, 4, 0.68), Edge(3, 8, 0.96)]: print ("pass")
    else: 
        print ("fail")        
    if weightSum == 4.34: print ("pass")
    else: 
        print ("fail")        
    print()


    g50 = WUGraph.fromFile("wugraph50.txt") 
    print("Prim eager on g50")
    edges, weightSum = mstPrimEager(g50)    
    failCorrectness = False     
    if weightSum == 82124: print ("pass")
    else: 
        print ("fail")
        failCorrectness = True
    print()

    if failCorrectness: print("fail")
    else:
        n = 100
        tKruskal = timeit.timeit(lambda: mstKruskal(g50), number=n)/n
        tPrimLazy = timeit.timeit(lambda: mstPrimLazy(g50), number=n)/n
        tPrimEager = timeit.timeit(lambda: mstPrimEager(g50), number=n)/n
        print(f"Average running time for g50 with Kruskal ({tKruskal:.10f}), PrimLazy ({tPrimLazy:.10f}), and PrimEager({tPrimEager:.10f})")        
        if tPrimEager * 3.0 < tKruskal and tPrimEager * 3.0 < tPrimLazy: print ("pass")
        else: print ("fail")
    print()
    
    