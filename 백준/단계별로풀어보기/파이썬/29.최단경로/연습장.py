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

def dijkstra(graph, start):
    distTo = [float('inf')] * (graph.V+1)
    edgeTo = [None] * (graph.V+1)
    visited = [False] * (graph.V+1)
    pq = []
    
    distTo[start] = 0
    heapq.heappush(pq, (distTo[start], start))
    
    while pq:
        dist, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        
        for edge in graph.adj[node]:
            if distTo[edge.w] > distTo[edge.v] + edge.weight:
                distTo[edge.w] = distTo[edge.v] + edge.weight
                edgeTo[edge.w] = edge.v
                heapq.heappush(pq, (distTo[edge.w], edge.w))
    
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