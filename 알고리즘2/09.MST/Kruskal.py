from queue import PriorityQueue

class Edge: # 간선 추가
    def __init__(self, v, w, weight):
        if v <= w: self.v, self.w = v, w
        else: self.v, self.w = w, v
        self.weight = weight
        
    def __lt__(self, other): # __less than__ : 비교 연산자가 사용되는 시점에 자동으로 호출됨.
        return self.weight < other.weight
    
    def __str__(self):
        return f"{self.v}-{self.w} ({self.weight})"
    
class WUGraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self.edges = []
        
    def addEdge(self, v, w ,weight):
        e = Edge(v,w,weight)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.edges.append(e)
        self.E += 1
        
class UF:
    def __init__(self, V):
        self.ids = list(range(V))
        self.size = [1] * V
        
    def root(self, i):
        while i != self.ids[i]:
            i = self.ids[i]
        return i
    
    def connected(self, v, w):
        return self.root(v) == self.root(w)
    
    def union(self, p, q):
        pass
    
def mstKruskal(g):
    assert(isinstance(g,WUGraph))
    mstEdge = []
    mstEdgeSum = 0
    
    pq = PriorityQueue()
    
    for edge in g.edges:
        pq.put(edge)
        
    uf = UF(g.V)
    while not pq.empty() and len(mstEdge) < g.V - 1:
        e = pq.get()
        if not uf.connected(e.v, e.w):
            uf.union(e.v, e.w)
            mstEdge.append(e)
            mstEdgeSum += e.weight
    
    return mstEdge, mstEdgeSum

if __name__ == "__main__":
    g = WUGraph(4)
    g.addEdge(0, 1, 1.0)
    g.addEdge(1, 2, 2.0)
    g.addEdge(0, 2, 3.0)
    g.addEdge(2, 3, 1.0)

    edges, totalWeight = mstKruskal(g)
    print("MST edges:")
    for e in edges:
        print(e)
    print("Total weight:", totalWeight)
