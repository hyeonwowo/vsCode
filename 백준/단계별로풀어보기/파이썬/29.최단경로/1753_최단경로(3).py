import sys
import heapq 

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
        
def relax(v, w, weight, edgeTo, distTo, pq):
    if distTo[w] > distTo[v] + weight:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(pq, (distTo[w], w))
        
def dijkstra(graph, start):
    distTo = [float('inf')] * (graph.v + 1)
    edgeTo = [None] * (graph.v + 1)
    visited = [False] * (graph.v + 1)
    
    distTo[start] = 0
    
    pq = []
    heapq.heappush(pq, (distTo[start], start))    
    
    while pq:
        distV, v = heapq.heappop(pq)
        if visited[v] == True:
            continue
        visited[v] = True
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo, pq)
            
    return distTo, edgeTo
    
if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    s = int(sys.stdin.readline())
    graph = Graph(V)
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        graph.addEdge(v, w, weight)
        
    distTo, edgeTo = dijkstra(graph, s)
    
    for i in range(1, V+1):
        if distTo[i] == float('inf'):
            print("INF")
        else:
            print(distTo[i])