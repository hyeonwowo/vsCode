import sys # dijkstra : 328ms
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
        
def relax(v, w, weight, edgeTo, distTo, heap):
    if distTo[v] != float('inf') and distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(heap, (distTo[w], w))

def dijkstra(start, graph):
    V = graph.V
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    distTo[start] = 0
    
    heap = []
    heapq.heappush(heap,(distTo[start], start))
    
    while heap:
        curr_dist, v = heapq.heappop(heap)
        
        if curr_dist > distTo[v]:
            continue
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo, heap)

    return edgeTo, distTo

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    
    g = Graph(V)
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
        
    start, end = map(int, sys.stdin.readline().split())
    
    edgeTo, distTo = dijkstra(start, g)
    print(distTo[end])