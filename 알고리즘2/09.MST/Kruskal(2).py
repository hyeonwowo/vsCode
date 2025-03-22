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
        
    
def mstKruskal(g):
    pass

if __name__ == "__main__":
    pass