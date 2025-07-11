import sys

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(self.V+1)]
        
    def addEdge(self, v, w, weight):
        self.adj[v].append((Edge(v, w, weight)))

def floadWarshell(graph):
    dist = [[float('inf')] * (V+1) for _ in range(V+1)]
    
    for i in range(1, V+1):
        dist[i][i] = 0
        
    for i in range(1, V+1):
        for j in range(1, V+1):
            v, w, weight = graph.adj[i]
            dist[i][j] = min(dist[i][j], weight)

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    
    g = Graph(V)
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
        