import sys
import heapq

# 최단경로 구하기
# 최단경로 엣지를 graph에서 지우기
# graph에서 다시 최단경로 구하기
# 끝.

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        
def relax(v, w, weight, edgeTo, distTo, pq):
    if distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(pq, (distTo[w], w))

def dijkstra(start, graph):
    V = graph.V
    edgeTo = [None] * V
    distTo = [float('inf')] * V
    pq = []
    
    distTo[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        curr_dist, v = heapq.heappop(pq)
        if distTo[v] < curr_dist:
            continue
        
        for edge in graph.adj[v]:
            relax(edge.v, edge.w, edge.weight, edgeTo, distTo, pq)
            
    return edgeTo, distTo

def pathTo(edgeTo, v):
    path = []
    while v is not None:
        path.append((v, edgeTo[v]))
        v = edgeTo[v]
    path.reverse()
    return path

if __name__ == "__main__":
    res = []
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break
        
        start, end = map(int, sys.stdin.readline().split())
        g = Graph(n)
        for _ in range(m):
            v, w, weight = map(int, sys.stdin.readline().split())
            g.addEdge(v, w, weight)
            
        edgeTo, _ = dijkstra(start, g)
        path = pathTo(edgeTo, end)
        
        for v, w in path:
            g.adj[v].remove(w)
          
        _, distTo = dijkstra(start, g)  
        res.append(distTo[end])
        
    for ele in res:
        print(ele)