import sys
from collections import deque

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        
class Graph:
    def __init__(self, V):
        self.v = V
        self.adj = [[] for _ in range(self.v+1)]
    
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        self.adj[w].append(Edge(w, v, weight))
        
    def BFS(self, start):
        visited = [False] * (self.v+1)
        dist = [0] * (self.v+1)
        queue = deque([start])
        
        visited[start] = True
        dist[start] = 0
        maxvertex = 0
        
        while queue:
            node = queue.popleft()
            for edge in self.adj[node]:
                if not visited[edge.w]:
                    visited[edge.w] = True
                    dist[edge.w] = dist[node] + edge.weight
                    queue.append(edge.w)
                    if dist[edge.w] > dist[maxvertex]:
                        maxvertex = edge.w
                        
        return maxvertex, dist[maxvertex]
        
    
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    graph = Graph(n)
    for _ in range(n-1):
        v, w, weight = map(int, sys.stdin.readline().split())
        graph.addEdge(v, w, weight)
    
    maxvertex, dist = graph.BFS(1)
    
    maxvertex, dist = graph.BFS(maxvertex)
    print(dist)