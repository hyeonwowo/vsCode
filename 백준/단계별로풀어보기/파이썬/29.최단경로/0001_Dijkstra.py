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
        self.adj = [[] for _ in range(V+1)] # 정점중심이라 adJ 자료구조 사용
        
    def addEdge(self, v, w, weight):
        self.adj[v].append(Edge(v, w, weight))
        
def relax(v, w, weight, distTo, edgeTo, pq):
    if distTo[v] + weight < distTo[w]:
        distTo[w] = distTo[v] + weight
        edgeTo[w] = v
        heapq.heappush(pq, (distTo[w], w))
        
def dijkstra(graph, start):
    V = graph.V
    distTo = [float('inf')] * (V+1)
    edgeTo = [None] * (V+1)
    distTo[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distTo[u]:
            continue
        
        for edge in graph.adj[u]:
            relax(edge.u, edge.v, edge.wiehgt, distTo, edgeTo, pq)
            
    return distTo, edgeTo

def pathTo(edgeTo, v):
    path = []
    while v is not None:
        path.append(v)
        v = edgeTo[v]
    path.reverse()
    return path

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 1)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 6, 4)
    g.add_edge(5, 6, 1)

    start = 1
    distTo, edgeTo = dijkstra(g, start)

    for v in range(1, g.V + 1):
        path = pathTo(edgeTo, v)
        if distTo[v] == float('inf'):
            print(f"{start} -> {v}: 도달 불가")
        else:
            print(f"{start} -> {v}: 거리={distTo[v]}, 경로={path}")


        
    