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
        
def relax(v, w, weight, distTo, edgeTo, pq):
    if distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(pq, (distTo[w], w))
        
def dijkstra(start, graph):
    V = graph.V
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    pq = []
    
    distTo[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        curr_dist, v = heapq.heappop(pq)
        if distTo[v] < curr_dist:
            continue
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo, pq)
            
    return distTo, edgeTo

if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    
    g = Graph(n)
    for _ in range(m):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
        
    distTo, edgeTo = dijkstra(1, g)
    for i in range(1, n+1):
        if distTo[i] >= float('inf'):
            print(-1)
        else:
            print(distTo[i])