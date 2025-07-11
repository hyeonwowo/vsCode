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
        self.adj[v].append(Edge(v, w, weight)) 

def floydWarshell(graph):
    V = graph.V
    dist = [[float('inf')] * (V+1) for _ in range(V+1)]
    
    for i in range(1, V+1):
        for edge in graph.adj[i]:
            dist[edge.v][edge.w] = min(dist[edge.v][edge.w], edge.weight)
    
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    minval = float('inf')
    for i in range(1, V+1):
        if minval > dist[i][i]:
            minval = dist[i][i]
            
    if minval == float('inf'):
        minval = -1
        
    return minval

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    g = Graph(V)
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
    
    dist = floydWarshell(g)
    print(dist)
    