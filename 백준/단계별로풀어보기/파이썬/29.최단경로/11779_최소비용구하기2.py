import sys # 시간초과
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
    if distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(heap, (distTo[w], w)) # 수정 : (w, distTo[w]) -> (distTo[w], w)

def dijkstra(start, graph):
    V = graph.V
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    distTo[start] = 0

    pq = []
    heapq.heappush(pq, (0, start)) # 수정 : (start, 0) -> (0, start)

    while pq:
        currdist, v = heapq.heappop(pq)

        if currdist > distTo[v]: 
            continue

        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo, pq)

    return edgeTo, distTo

def pathTo(v, edgeTo):
    path = []
    while v is not None:
        path.append(v)
        v = edgeTo[v]
    path.reverse()
    return path

if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    
    g = Graph(V)
    for _ in range(E):
        v, w, weight = map(int, sys.stdin.readline().split())
        g.addEdge(v, w, weight)
        
    start, end = map(int, sys.stdin.readline().split())
    
    edgeTo, distTo = dijkstra(start, g)
    citypath = pathTo(end, edgeTo)
    
    print(distTo[end])
    print(len(citypath))
    print(*citypath)