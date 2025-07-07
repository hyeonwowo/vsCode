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
        self.adj = [[] for _ in range(self.V + 1)]
        
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        self.adj[w].append(Edge(w, v, weight))
        
def relax(v, w, weight, edgeTo, distTo, pq):
    if distTo[w] > distTo[v] + weight:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v 
        heapq.heappush(pq, (distTo[w], w))
    
def dijkstra(start, graph):
    edgeTo = [None] * (graph.V + 1)
    distTo = [float('inf')] * (graph.V + 1)
    visited = [False] * (graph.V + 1)
    pq = []
    
    distTo[start] = 0
    heapq.heappush(pq, (distTo[start], start))
    
    while pq:
        dist, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo, pq)
        
    return edgeTo, distTo

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    
    graph = Graph(V)
    start = 1
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        graph.addEdge(v, w, weight)
        
    a, b = map(int, sys.stdin.readline().split())
    
    # 세번의 다익스트라 실행
    # 1 - a - b - t
    # 1 - b - a - t

    _ , distTo = dijkstra(start, graph)
    _ , distToA = dijkstra(a, graph)
    _ , distToB = dijkstra(b, graph)
    
    pathA = distTo[a] + distToA[b] + distToB[V]
    pathB = distTo[b] + distToB[a] + distToA[V]
    
    result = min(pathA, pathB)
    if result == float('inf'):
        print(-1)
    else:
        print(result)
    
   