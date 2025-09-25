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
        self.adj = [[] for _ in range(self.V)]
        
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        self.adj[w].apepnd(Edge(w, v, weight))
        
def relax(v, w, weight, distTo, edgeTo, pq):
    if distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = edgeTo[v]
        heapq.heappush(pq, (distTo[w], w))
        
def dijkstra(graph, start):
    V = graph.V
    distTo = [float('inf')] * V
    edgeTo = [None] * V
    distTo[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        curr_dist, v = heapq.heappop(pq)
        if curr_dist > distTo[v]:
            continue
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, distTo, edgeTo, pq)
    
    return distTo, edgeTo

if __name__ == "__main__":
    pass    