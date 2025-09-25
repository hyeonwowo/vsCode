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
        
def relax(v, w, weight, distTo, pq, k):
    new_dist = v + weight
    if len(distTo[w]) < k:
        heapq.heappush(distTo[w], -new_dist)
        heapq.heappush(pq, (new_dist, w))
    else:
        if -distTo[w][0] > new_dist:
            heapq.heappop(distTo[w])
            heapq.heappush(distTo[w], -new_dist)
            heapq.heappush(pq, (new_dist, w))

def dijkstra(start, graph, k):
    V = graph.V
    distTo = [[] for _ in range(V+1)]
    pq = []
    
    heapq.heappush(distTo[start], 0)
    heapq.heappush(pq, (0, start))
    
    while pq:
        curr_dist, v = heapq.heappop(pq)
        
        for edge in graph.adj[v]:
            relax(curr_dist, edge.w, edge.weight, distTo, pq, k)
            
    return distTo

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    
    g = Graph(n)
    for _ in range(m):
        v, w, weight = map(int, input().split())
        g.addEdge(v, w, weight)
        
    distTo = dijkstra(1, g, k)
    
    for i in range(1, n+1):
        if len(distTo[i]) < k:
            print(-1)
        else:
            print(-distTo[i][0])  # k번째 최단경로
