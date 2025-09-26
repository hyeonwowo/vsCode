import sys
import heapq

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V+1)]
        
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        
def relax():
    pass

def dijkstra():
    pass

if __name__ == "__main__":
    N, M, x, y = map(int, sys.stdin.readline().split())
    g = Graph(N)
    
    for _ in range(M):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
        
        