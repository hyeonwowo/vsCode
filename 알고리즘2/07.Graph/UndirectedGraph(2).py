from queue import Queue

class Graph:
    def __init__(self,V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        
    def adEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
        
    def degree(self, v):
        return len(self.adj[v])
    
    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for w in self.adj[v]:
                if v <= w: rtList.append(f"{v}-{w}\n")
        return "".join(rtList)