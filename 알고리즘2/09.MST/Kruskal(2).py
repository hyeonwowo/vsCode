from queue import PriorityQueue

class Edge:
    def __init__(self,v, w, weight):
        if v <= w: self.v, self.w = v, w
        else: self.v, self.w = w, v
    def __lt__(self, other):
        return self.weight < other.weight
    def __str__(self):
        return f"{self.v}-{self.w} ({self.weight})"
    
class WUGraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self.edges = []
        
    def addEdge(self, v, w, weight):
        e = Edge(v, w, weight)
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.edges.append(e)
        self.E += 1
        
class UF:
    def __init__(self, V):
        self.ids = list(range(V))
        self.size = [1] * V
        
    def root(self, i):
        while i != self.ids[i]:
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        root_p, root_q = self.root(p), self.root(q)
        if self.size[root_p] >= self.size[root_q]:
            self.ids[root_q] = root_p
            self.size[root_p] += root_q
        else:
            self.ids[root_p] = root_q
            self.size[root_q] += root_p
    
def mstKruskal(g):
    assert(isinstance(g,WUGraph))
    mstEdge = []
    mstEdgeSum = 0
    
    pq = PriorityQueue()
    for e in g.edges:
        pq.put(e)
    
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