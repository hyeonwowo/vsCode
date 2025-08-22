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
        self.adj[w].append(Edge(w, v, weight))  # 수정됨
        
def relax(v, w, weight, edgeTo, distTo, heap):
    if distTo[v] != float('inf') and distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(heap, (distTo[w], w))   # 수정됨
        
def dijkstra(start, graph):
    V = graph.V
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    distTo[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        currdist, v = heapq.heappop(heap)
        
        if currdist > distTo[v]:
            continue
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo, heap)
            
    return edgeTo, distTo

def pathTo(v, edgeTo):
    path = []
    while v is not None:
        path.append(v)
        v = edgeTo[v]
    path.reverse()
    return path

if __name__ == "__main__":
    V, E, P = map(int, sys.stdin.readline().split())
    g = Graph(V)
    
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
    
    edgeTo_A, distTo_A = dijkstra(1, g)
    edgeTo_B, distTo_B = dijkstra(P, g)
    
    AB = distTo_A[V]
    APB = distTo_A[P] + distTo_B[V]
    
    if AB == APB:
        print("SAVE HIM")
    else:
        print("GOOD BYE")
